import requests
import streamlit as st

def get_ollama_response(input_text):
    response = requests.post(
        "http://localhost:8000/poem/invoke",
        json={"input": {"topic": input_text}}
    )
    return response.json()['output']

st.title("Ollama Poem Generator")
input_text = st.text_input("Enter a topic for the poem:")

if input_text:
    try:
        response = get_ollama_response(input_text)
        st.text_area("Generated Poem:", value=response['poem'], height=300)
    except Exception as e:
        st.error(f"Error: {str(e)}")
