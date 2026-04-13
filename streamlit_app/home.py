"""
Home page for Streamlit authentication interface.
No external auth server required — session managed locally.
"""

import uuid
import streamlit as st

# Hide sidebar nav for cleaner look
hide_sidebar_style = """
    <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)

st.set_page_config(page_title="LangGraph Chat - Login")

st.title("🔐 Welcome to LangGraph Assistant")

# If already logged in, redirect to chat
if "session_id" in st.session_state and "username" in st.session_state:
    st.switch_page("pages/chat.py")

# Login / signup form
with st.form("auth_form"):
    username = st.text_input("Username")
    submit = st.form_submit_button("Enter Chat")

if submit:
    if not username:
        st.error("Please enter a username.")
    else:
        # Generate a unique session ID based on username
        st.session_state["session_id"] = f"{username}-{uuid.uuid4().hex[:8]}"
        st.session_state["username"] = username
        st.success(f"Welcome, {username}! Redirecting to chat...")
        st.switch_page("pages/chat.py")
