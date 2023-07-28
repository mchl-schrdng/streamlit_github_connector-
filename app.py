# app.py

import streamlit as st
from src.github_connector import GitHubConnection

# Create an instance of the GitHubConnection with a connection name
conn = GitHubConnection("github")

# Add a button to the Streamlit app
if st.button('Extract GitHub Activity'):
    # Use the connection to fetch user's GitHub activity when the button is clicked
    user_activity = conn.get_user_activity("your_github_username")
    
    # Display the result in Streamlit
    st.dataframe(user_activity)
