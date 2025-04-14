import os
from google import genai
from google.genai import types
from dotenv import load_dotenv


load_dotenv()

client = genai.Client(api_key=os.getenv('GEMINI_APIKEY'))


def load_config_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip() and not line.startswith("#")]
    except FileNotFoundError:
        return []


def read_project_code(project_path):
    extensions = load_config_file("extensions.cfg")
    ignored_dirs = load_config_file("ignore_dirs.cfg")

    code_contents = []
    for root, dirs, files in os.walk(project_path):
        if any(ignored in root for ignored in ignored_dirs):
            continue
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, project_path)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    code_contents.append(f"### file: {relative_path}\n{content}\n")
                except Exception as e:
                    print(f"Error reading {relative_path}: {e}")
    return '\n'.join(code_contents)


async def run_gemini(code_text, prompt):
    contents = [
        types.Part.from_bytes(
            data=code_text.encode("utf-8"),
            mime_type="text/plain",
        ),
        prompt,
    ]

    chat = client.aio.chats.create(
        model="gemini-2.5-pro-exp-03-25",
        config=types.GenerateContentConfig(
            tools=[types.Tool(code_execution=types.ToolCodeExecution)]
        ),
    )

    response = await chat.send_message(contents)
    return response.text
