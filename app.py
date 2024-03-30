import os
import streamlit as st
import google.generativeai as genai

try:
    gemini_api_key = os.environ['GOOGLE_GEMINI_KEY']
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-pro')

    if "chat" not in st.session_state:
      st.session_state.chat = model.start_chat(history=[])
    st.title('Gemini Pro Test')

    def role_to_streamlit(role: str) -> str:
      if role == 'model':
        return 'assistant'
      else:
        return role

    for message in st.session_state.chat.history:
      with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

    if prompt := st.chat_input("I possess a well of knowledge. What would you like to know?"):
      st.chat_message("user").markdown(prompt)
      response = st.session_state.chat.send_message(prompt)
      with st.chat_message("assistant"):
        st.markdown(response.text)
except Exception as e:
    st.error(f'An error occurred: {e}')
