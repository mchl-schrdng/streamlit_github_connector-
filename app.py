import streamlit as st

# Create the GitHub connection
conn = st.experimental_connection('github', type='github')

# Use the connection to fetch user's GitHub activity
user_activity = conn.get_user_activity(your_github_username)

st.write(user_activity)
