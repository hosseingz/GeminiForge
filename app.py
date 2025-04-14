import streamlit as st
import asyncio

from utils import read_project_code, run_gemini


st.set_page_config(page_title="GeminiForge", layout="centered")
st.title("🎯 GeminiForge")

st.markdown("""
GeminiForge analyzes your codebase based on a given project path and prompt.  
It reads the project's source files and queries the Gemini AI model  
to provide intelligent responses or code modifications.
""")


project_path = st.text_input("📁 Project Path:")
prompt = st.text_area("📝 Prompt for the Gemini Model:")

rtl_enabled = st.checkbox("Enable Right-to-Left (RTL) Display")


# RTL or LTR styling
if rtl_enabled:
    st.markdown("""
        <style>
        body, .stTextInput, .stTextArea, .stButton, .stMarkdown, .stTitle {
            direction: rtl;
            text-align: right;
        }
        </style>
        """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        body, .stTextInput, .stTextArea, .stButton, .stMarkdown, .stTitle {
            direction: ltr;
            text-align: left;
        }
        </style>
        """, unsafe_allow_html=True)



if st.button("🚀 Run"):
    if not project_path or not prompt:
        st.error("⚠️ Please provide both the project path and the prompt.")
    else:
        with st.spinner("Processing code with the Gemini model..."):
            try:
                code_text = read_project_code(project_path)
                response_text = asyncio.run(run_gemini(code_text, prompt))

                st.success("✅ Response received:")
                st.markdown(response_text)

            except Exception as e:
                st.error(f"❌ An error occurred: {e}")
