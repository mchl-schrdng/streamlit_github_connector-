# src/github_connector.py

from streamlit.connections import ExperimentalBaseConnection
import streamlit as st

class GitHubConnection(ExperimentalBaseConnection):

    def __init__(self, connection_name):
        super().__init__(connection_name)

    def _connect(self, **kwargs):
        self.token = st.secrets['github']['token']
        return self

    def get_user_activity(self, username):
        # Implement the logic to fetch user activity from GitHub
        pass
