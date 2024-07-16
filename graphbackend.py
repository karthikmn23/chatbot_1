# backend_notebook

import openai
import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO

# Set up OpenAI API key
openai.api_key = 'your_openai_api_key'

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

# Function to generate plots based on the query
def generate_plot(df, plot_type, x_col, y_col=None, hue=None):
    plt.figure()
    if plot_type == 'histogram':
        sns.histplot(df[x_col])
    elif plot_type == 'line':
        sns.lineplot(data=df, x=x_col, y=y_col, hue=hue)
    elif plot_type == 'box':
        sns.boxplot(data=df, x=x_col, y=y_col, hue=hue)
    elif plot_type == 'scatter':
        sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue)
    elif plot_type == 'bar':
        sns.barplot(data=df, x=x_col, y=y_col, hue=hue)
    elif plot_type == 'heatmap':
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    else:
        return None

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()
    return image_base64

# Function to handle user queries
def handle_user_query(user_query):
    # Query your table and get the data
    df = query_database("SELECT * FROM your_table")
    
    # Use OpenAI to interpret the query and determine plot type and columns
    prompt = f"Analyze the following data: {df.head().to_string()}\n\nBased on the user's query: '{user_query}', determine the plot type and relevant columns for visualization."
    response = query_openai(prompt)
    
    # Parse the response to extract plot type and columns
    plot_type = 'histogram'  # Example: extract this from the response
    x_col = 'column_name'    # Example: extract this from the response
    y_col = None             # Example: extract this from the response if applicable
    hue = None               # Example: extract this from the response if applicable
    
    # Generate the plot if the query indicates a plot
    if plot_type:
        plot_image = generate_plot(df, plot_type, x_col, y_col, hue)
        return plot_image
    else:
        # Convert the dataframe to a string or relevant format
        data_str = df.to_string()
        combined_text = f"Database content:\n{data_str}\n\nUser query: {user_query}"
        response = query_openai(combined_text)
        return response

# Accept parameters
dbutils.widgets.text("user_query", "")
user_query = dbutils.widgets.get("user_query")

# Run the function and return the result
response = handle_user_query(user_query)
print(response)
Frontend Notebook (frontend_notebook)
python
Copy code