# Conversational Q&A Chatbot Using Gemini-Pro Model
- This project demonstrates a **Conversational Q&A Chatbot** application powered by the **Gemini 1.5 Pro Large Language Model (LLM)**. Built using Streamlit, this chatbot allows users to interact with the model, ask questions, and receive intelligent responses. The chatbot also maintains a history of user-bot interactions for a seamless conversational experience.

### Features
**Conversational Interface:** Supports real-time Q&A through an intuitive text input field.
**Session Management:** Maintains a chat history for the session, allowing users to revisit previous conversations.
**Streaming Responses** Displays responses incrementally, mimicking a natural conversation flow.
**Powered by Gemini 1.5 Pro:** Leverages Google's cutting-edge LLM for accurate and context-aware responses.

### Technologies Used
**Streamlit:** Frontend framework for building the interactive web application.
**Google Generative AI API:** Integrates the Gemini 1.5 Pro LLM for generating responses.
**Python:** Backend logic and API interactions.
**dotenv:** Manages environment variables securely.

### How It Works
**1.User Input:** Users can type questions in the input box.
**Generate Response:** The get_response function sends the question to the Gemini 1.5 Pro model, processes the response, and streams it back to the user.
**Chat History:** Maintains a history of interactions, displayed at the bottom of the application interface.
