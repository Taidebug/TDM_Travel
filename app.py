import os
from pathlib import Path
import streamlit as st
from dotenv import load_dotenv
from rag import answer_question

from firebase_client import authenticate

env_path = Path(__file__).with_name(".env")
load_dotenv(env_path)
api_key = os.getenv("FIREBASE_API_KEY")

st.set_page_config(page_title="TDM Travel")
if "user" not in st.session_state:
    st.session_state["user"] = None

if "messages" not in st.session_state:
    st.session_state["messages"] = []

st.title("TDM Travel")
st.write("Travel assistant in Thu Dau Mot")

def display_message(message):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message.get("sources"):
            with st.expander("Xem các mục được truy xuất"):
                for result in message["sources"]:
                    entry = result["entry"]
                    score = result["score"]

                    st.markdown(
                        f"**[{entry['id']}] {entry['title']}**"
                    )
                    st.caption(f"Cosine similarity: {score:.4f}")
                    st.write(entry["text"])
                    st.markdown(
                        f"[Mở nguồn tham khảo]({entry['source']})"
                    )

if st.session_state["user"] is None:
    mode = st.radio("Account", ["Login", "Sign up"], horizontal=True)
    with st.form("auth_form", clear_on_submit=True):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = ""
        if mode == "Sign up":
            confirm_password = st.text_input("Confirm password", type="password")

        submitted = st.form_submit_button(mode)

    if submitted:
        if not email.strip() or not password:
            st.error("Please enter correct email or password")
        elif not api_key:
            st.error("Missing FIREBASE_API_KEY")
        elif mode == "Sign up" and password != confirm_password:
            st.error("Passwords do not match")
        else:
            try:
                user = authenticate(api_key, email.strip(), password, sign_up=(mode == "Sign up"))
            except ValueError as error:
                st.error(str(error))
            else:
                st.session_state["user"] = user
                st.rerun()

else:
    user = st.session_state["user"]

    st.success("You are signed in.")
    st.write("Email: ", user["email"])

    if st.button("Sign out"):
        st.session_state["user"] = None
        st.session_state["messages"] = []
        st.rerun()

    st.subheader("Travel Assistant")

    for message in st.session_state["messages"]:
        display_message(message)

    question = st.chat_input("Hỏi về địa điểm ở Thủ Dầu Một...")

    if question is not None:
        question = question.strip()

        if not question:
            st.warning("Vui lòng nhập câu hỏi.")
        else:
            try:
                with st.spinner("Đang tìm nguồn và tạo câu trả lời..."):
                    answer, results = answer_question(question, k=3)

            except (ValueError, OSError) as error:
                st.error(str(error))

            else:
                st.session_state["messages"].append({
                    "role": "user",
                    "content": question
                })

                st.session_state["messages"].append({
                    "role": "assistant",
                    "content": answer,
                    "sources": results
                })

                st.rerun()
    