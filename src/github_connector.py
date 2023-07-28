import streamlit as st
from streamlit.connections import ExperimentalBaseConnection
import requests

class GitHubConnection(ExperimentalBaseConnection):

    BASE_URL = "https://api.github.com"

    def __init__(self, connection_name):
        super().__init__(connection_name)
        self.token = st.secrets["github"]["token"]

    def _connect(self):
        return self

    def _make_request(self, endpoint, params=None):
        url = f"{self.BASE_URL}{endpoint}"
        headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json"
        }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error {response.status_code}: {response.text}")
            return []

    def get_user_profile(self, username):
        return self._make_request(f"/users/{username}")

    #def get_user_activity(self, username):
        #return self._make_request(f"/users/{username}/events/public")

    def get_user_activity(self, username, max_pages=5):
        activities = []
        for page in range(1, max_pages + 1):
            endpoint = f"/users/{username}/events/public"
            params = {
                "per_page": 100,
                "page": page
            }
            results = self._make_request(endpoint, params=params)
            if not results:
                break
            activities.extend(results)
        return activities

    def get_user_repositories(self, username):
        return self._make_request(f"/users/{username}/repos")

    def get_user_issues(self, username):
        return self._make_request(f"/search/issues?q=author:{username}")

    def get_user_pull_requests(self, username):
        return self._make_request(f"/search/issues?q=author:{username} type:pr")

    def get_user_starred_repos(self, username):
        return self._make_request(f"/users/{username}/starred")

    def get_user_followers(self, username):
        return self._make_request(f"/users/{username}/followers")

    def get_user_following(self, username):
        return self._make_request(f"/users/{username}/following")

    def get_user_gists(self, username):
        return self._make_request(f"/users/{username}/gists")

    def get_user_organizations(self, username):
        return self._make_request(f"/users/{username}/orgs")

    def get_repo_languages(self, owner, repo):
        return self._make_request(f"/repos/{owner}/{repo}/languages")
