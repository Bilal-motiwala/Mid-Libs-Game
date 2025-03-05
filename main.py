import streamlit as st

# Streamlit App Title
st.title("🎭 Mad Libs Game")

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
