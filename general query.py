import streamlit as st
from openai import OpenAI
import os
gpt_api_key = os.environ.get('GPT_API_key')
user= OpenAI(api_key=gpt_api_key)
userrole = "user"
st.title("General search")
input_text= st.text_input("What would you like to learn more about?")
button = st.button("search")
if button:
    response = user.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages= [
            {"role": userrole, "content": input_text}
        ]
    )
    st.write(response.choices[0].message.content)