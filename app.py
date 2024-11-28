import streamlit as st
from model import get_response

## initialize streamlit app

st.set_page_config(page_title="Conversational Q&A ChatBOT Demo")

st.header("Gemini 1.5 Pro LLM Application")

# Initialize the session for chat history recording If it doesn't exist

if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]


input = st.text_input("Input:",key ="input")
submit=st.button("Ask the question")


if submit and input:
    response= get_response(input)

    ## Adding the user query and response to session state chat hostory
    st.session_state['chat_history'].append(("You",input))
    st.subheader("The response is")

    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot:",chunk.text))
    st.subheader("The chat history is")

for role, text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")