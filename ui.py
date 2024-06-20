import streamlit as st
from main import genai_engine, MODEL_IDS

# Include Bootstrap
st.markdown(
    """
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
    .stApp {
        background-image: url('https://www.politico.com/dims4/default/b07a49c/2147483647/strip/true/crop/1160x773+0+0/resize/1290x860!/format/webp/quality/90/?url=https%3A%2F%2Fstatic.politico.com%2F8c%2F18%2F7fb9b88e4e588a4cc84bb8da9bbf%2F200613-nyt-getty-773.jpg');  /* Newspaper background */
        background-size: cover;
        color: #800000;
    }
    h1 {
        color: #FF0000; /* Maroon color for heading */
    }
       .input-label {
       color: #800000; /* Maroon color for "What is up?" text */
    }
    .chat-container {
        max-width: 700px;
        margin: auto;
        padding: 20px;
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        margin-top: 20px;
    }
    .user-message {
        background-color: #d1e7dd;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .assistant-message {
        background-color: #f8d7da;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .response-true {
        color: green;
        font-weight: bold;
    }
    .response-fake {
        color: red;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='text-center'>FakeBot Buster</h1>", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to style chat messages
def style_message(role, content, label):
    if role == "user":
        return f"<div class='user-message'><strong>User:</strong> {content}</div>"
    else:
        response_class = "response-true" if label.lower() in ["true", "real"] else "response-fake"
        return f"<div class='assistant-message'><strong>Assistant:</strong> <span class='{response_class}'>{content}</span></div>"

# Display chat messages from history on app rerun
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
for message in st.session_state.messages:
    st.markdown(style_message(message["role"], message["content"], message.get("label", "")), unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Model selection dropdown
model_name = st.selectbox("Select a model to use:", list(MODEL_IDS.keys()))

# React to user input
if prompt := st.text_input("What is up?", key="input"):
    # Display user message in chat message container
    st.markdown(f"<div class='chat-container'>{style_message('user', prompt, '')}</div>", unsafe_allow_html=True)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response, reasoning, processing_time = genai_engine(prompt, model_name)
    response_message = f"Response: {response}<br><span style='color: #0d6efd;'>Reasoning:</span> {reasoning}<br><span style='color: #20c997;'>Processing time:</span> {processing_time:.2f} seconds"
    label = "true" if response.lower() in ["true", "real"] else "fake"
    st.markdown(f"<div class='chat-container'>{style_message('assistant', response_message, label)}</div>", unsafe_allow_html=True)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response_message, "label": label})
