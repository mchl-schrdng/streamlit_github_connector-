# app.py

import streamlit as st
from src.github_connector import GitHubConnection

# Create an instance of the GitHubConnection
conn = GitHubConnection()

# Use the connection to fetch user's GitHub activity
user_activity = conn.get_user_activity("your_github_username")
st.write(user_activity)
