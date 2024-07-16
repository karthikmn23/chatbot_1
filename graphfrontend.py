# frontend_notebook

import streamlit as st
import base64

st.title("Database Chatbot")
st.write("Ask questions related to the database content.")

user_query = st.text_input("Enter your query:")

if user_query:
    # Define the function to call the backend notebook
    def call_backend_notebook(query):
        # Define the notebook path
        backend_notebook_path = "/Users/your_email@example.com/backend_notebook"

        # Define the input parameters
        params = {"user_query": query}

        # Call the notebook
        result = dbutils.notebook.run(backend_notebook_path, 60, params)
        return result

    # Call the backend notebook with the user query
    response = call_backend_notebook(user_query)
    
    # Check if the response is a base64-encoded image
    try:
        img_data = base64.b64decode(response)
        st.image(img_data)
    except:
        # Display the response as text if it's not an image
        st.write("Response:", response)