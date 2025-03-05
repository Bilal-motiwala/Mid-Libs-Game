import streamlit as st
import streamlit.components.v1 as components

# Streamlit App Title
st.markdown(
    """
    <h1 style='text-align: center; color: #ff7e5f;'>🎭 Mad Libs Game Presented by Bilal Motiwala </h1>
    """,
    unsafe_allow_html=True
)

# Styling for responsiveness and attractiveness
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, #ff7e5f, #feb47b);
        font-family: Arial, sans-serif;
    }
    .stApp {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    .stTextInput input {
        width: 100%;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #ccc;
    }
    .stButton>button {
        background-color: #ff7e5f;
        color: white;
        padding: 10px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #feb47b;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Form for user input
st.write("Fill in the blanks below to generate your Mad Libs story!")

noun = st.text_input("Enter a noun:")
adjective = st.text_input("Enter an adjective:")
verb = st.text_input("Enter a verb:")
adverb = st.text_input("Enter an adverb:")

# Button to generate story
if st.button("Generate Story"):
    if noun and adjective and verb and adverb:
        story = f"One day, a {adjective} {noun} decided to {verb} {adverb}. It was a sight to see!"
        st.success(story)
    else:
        st.warning("Please fill in all fields before generating your story.")