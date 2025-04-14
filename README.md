# GeminiForge

GeminiForge is a powerful tool that analyzes your codebase based on a given project path and a prompt. It reads the project's source files and queries the **Gemini AI model** to provide intelligent responses or code modifications. You can integrate GeminiForge with your project for tasks like code review, refactoring, and AI-assisted development.

## Features 🚀

- **Codebase Analysis**: Scans project files and processes them based on file extensions and directories.
- **Gemini Model Integration**: Uses the Gemini AI model to generate intelligent responses or modify code based on your input prompt.
- **RTL/LTR Support**: Toggle Right-to-Left text direction for different languages (e.g., Arabic, Hebrew).
- **Interactive UI**: Built with Streamlit for an easy-to-use interface to run and visualize results.

## Setup Instructions 🛠️

### Prerequisites

- Python 3.7 or higher
- Google Gemini API key (see below for how to get one)
- Dependencies (listed in `requirements.txt`)

### Step 1: Clone the repository

```bash
git clone https://github.com/hosseingz/GeminiForge.git
cd geminiforge
```

### Step 2: Install dependencies

Use pip to install the required libraries from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 3: Set up the `.env` file

You need to create a `.env` file in the project root directory to store your **Google Gemini API key**.

1. Go to [Google AI Studio](https://aistudio.google.com/) and sign up/login.
2. Navigate to the **API Key** section.
3. Create and copy your API key.

Now, create a `.env` file in your project folder and add the following line:

```plaintext
GEMINI_APIKEY=your_api_key_here
```

### Step 4: Running the app

To run the Streamlit app, use the following command:

```bash
streamlit run app.py
```

This will start the web interface, where you can input the project path and a prompt for the Gemini model to analyze.

---

## Configuration Files

- `extensions.cfg`: Contains the file extensions that GeminiForge will consider during code analysis (e.g., `.py`, `.js`).
- `ignore_dirs.cfg`: Contains directories to exclude from analysis (e.g., `.git`, `.venv`).

You can modify these files to include or exclude certain file types or directories based on your project structure.

## How It Works 🔧

- **`app.py`**: This file contains the main logic for the Streamlit UI. Users can input the project path and a prompt, which is then sent to the Gemini model for processing.
- **`utils.py`**: Contains utility functions such as reading project files and interacting with the Gemini API. The `read_project_code()` function walks through the project directory, gathering code content, and `run_gemini()` sends the content to Gemini for processing.
- **`extensions.cfg` and `ignore_dirs.cfg`**: These configuration files allow you to define which file types should be analyzed and which directories should be ignored.

---

## Troubleshooting ⚠️

- **Missing `.env` file**: Ensure you've created the `.env` file and added the correct Gemini API key.
- **Error reading files**: If certain files cannot be read, check the file permissions or encoding issues.
- **Connection issues**: Make sure your internet connection is stable and your API key is valid.

---

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.