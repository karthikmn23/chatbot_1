import streamlit as st
import pandas as pd
import requests

# Function to handle user input and generate response
def handle_input(user_input):
    if "chart" in user_input.lower():
        # Generate chart
        st.write("Generating chart...")
        # Assume df is your Spark DataFrame converted to Pandas
        df = spark.read.format("your_format").option("your_options").load("your_table").toPandas()
        st.line_chart(df)
    else:
        # Generate text response
        st.write("Generating text response...")
        response = requests.post('http://localhost:5000/generate', json={'prompt': user_input})
        st.write(response.json())

st.title("Azure OpenAI and Streamlit App")

user_input = st.text_input("Enter your query:")
if st.button("Submit"):
    handle_input(user_input)