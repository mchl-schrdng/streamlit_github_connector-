import streamlit as st
from src.github_connector import GitHubConnection

# Create an instance of the GitHubConnection with a connection name
conn = GitHubConnection("github")

# Add a title to the sidebar
st.sidebar.title("GitHub Activity Extractor 😃")

# Create a text input box for the GitHub username in the sidebar
github_username = st.sidebar.text_input("Enter GitHub Username:")

# Add a button to the sidebar
if st.sidebar.button('Extract GitHub Activity') and github_username:
    # Use the connection to fetch user's GitHub activity for the provided username
    user_activity = conn.get_user_activity(github_username)
    
    # Display the result in the main area
    st.dataframe(user_activity)
