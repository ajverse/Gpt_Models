import streamlit as st
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🤖 DeepSeek Chatbot")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask me anything...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
        extra_body={},
        model="deepseek/deepseek-r1:free",
        messages=[{"role": "user", "content": user_input}]
    )

    bot_reply = completion.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    with st.chat_message("assistant"):
        st.write(bot_reply)