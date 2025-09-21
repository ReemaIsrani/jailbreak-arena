import os
import streamlit as st

if "initialized" not in st.session_state:
    os.environ["STREAMLIT_SERVER_ENABLE_FILE_WATCHER"] = "false"

    import torch
    torch.classes.__path__ = []

    if os.path.exists(".env"):
        from dotenv import load_dotenv
        load_dotenv()

    HF_TOKEN = os.environ.get("HF_TOKEN")
    if HF_TOKEN:
        try:
            print("Trying to login to hugging face")
            from huggingface_hub import login
            login(HF_TOKEN)
            print("Login to Hugging face was successful")
        except Exception as e:
            st.warning(f"Failed to login with HF_TOKEN: {e}")
    else:
        st.warning(
            "HF_TOKEN not set. "
            "Set it in .env (for local) or in HF Secrets (for hosting)."
        )

    st.session_state.initialized = True

if "chat_ui" not in st.session_state:
    try:
        from interface.chat_ui import ChatUI
        st.session_state.chat_ui = ChatUI()
    except Exception as e:
        st.error(f"Failed to initialize ChatUI: {e}")

try:
    st.session_state.chat_ui.launch()
except Exception as e:
    st.error(f"App failed to launch: {e}")
