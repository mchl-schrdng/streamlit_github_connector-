# app.py

import streamlit as st
from src.github_connector import GitHubConnection

# Create an instance of the GitHubConnection with a connection name
conn = GitHubConnection("github")

# Use the connection to fetch user's GitHub activity
user_activity = conn.get_user_activity("mchl-schrdng")
st.write(user_activity)
