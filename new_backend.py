# backend_notebook

import openai
import pyodbc
import pandas as pd

# Set up OpenAI API key
openai.api_key = "api_key"

# Set up database connection
def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=your_server;'
        'DATABASE=your_database;'
        'UID=your_username;'
        'PWD=your_password'
    )
    return conn

# Query the database
def query_database(query):
    conn = get_db_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Function to interact with OpenAI
def query_openai(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Function to handle user queries
def handle_user_query(user_query):
    # Query your table and get the data
    df = query_database("SELECT * FROM your_table")
    
    # Convert the dataframe to a string or relevant format
    data_str = df.to_string()

    # Combine the data and the user query
    combined_text = f"Database content:\n{data_str}\n\nUser query: {user_query}"
    
    # Get response from OpenAI
    response = query_openai(combined_text)
    return response

# Accept parameters
dbutils.widgets.text("user_query", "")
user_query = dbutils.widgets.get("user_query")

# Run the function and return the result
response = handle_user_query(user_query)
print(response)