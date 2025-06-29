import os
import streamlit as st

if __name__ == '__main__':
    if "initialized" not in st.session_state:
        os.environ["STREAMLIT_SERVER_ENABLE_FILE_WATCHER"] = "false"

        import torch
        torch.classes.__path__ = []

        from dotenv import load_dotenv
        from huggingface_hub import login
        load_dotenv()
        login(os.getenv("HUGGINGFACEHUB_API_TOKEN"))

        st.session_state.initialized = True

    if "chat_ui" not in st.session_state:
        from interface.chat_ui import ChatUI
        st.session_state.chat_ui = ChatUI()
    st.session_state.chat_ui.launch()
