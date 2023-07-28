import streamlit as st
from streamlit.connections import ExperimentalBaseConnection

class GitHubConnection(ExperimentalBaseConnection):

    def __init__(self, connection_name):
        super().__init__(connection_name)
        self.token = st.secrets["github"]["token"]

    def _connect(self):
        # No persistent connection is established with GitHub API, so we just return self
        return self

    def get_user_activity(self, username):
        # Construct the URL for the GitHub API request
        url = f"https://api.github.com/users/{username}/events/public"
        
        headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        # Use the ExperimentalBaseConnection to make the API call
        response = self.get(url, headers=headers)
        
        # Handle the response and return the data
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error {response.status_code}: {response.text}")
            return []
