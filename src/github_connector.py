import streamlit as st
from src.github_connector import GitHubConnection

# Create an instance of the GitHubConnection
conn = GitHubConnection("github")

# Sidebar
st.sidebar.title("GitHub User Explorer 🚀")
github_username = st.sidebar.text_input("Enter GitHub Username:")
if st.sidebar.button('Fetch Data 🕵️'):
    if github_username:
        # Fetch data using the GitHubConnection methods
        profile = conn.get_user_profile(github_username)
        activity = conn.get_user_activity(github_username)
        repos = conn.get_user_repositories(github_username)
        issues = conn.get_user_issues(github_username)
        pull_requests = conn.get_user_pull_requests(github_username)
        starred_repos = conn.get_user_starred_repos(github_username)
        followers = conn.get_user_followers(github_username)
        following = conn.get_user_following(github_username)
        gists = conn.get_user_gists(github_username)
        orgs = conn.get_user_organizations(github_username)

        # Display data as dataframes
        st.subheader(f"Profile of {github_username}")
        st.dataframe(profile)

        st.subheader("Recent Activity")
        st.dataframe(activity)

        st.subheader("Repositories")
        st.dataframe(repos)

        st.subheader("Issues Created")
        st.dataframe(issues)

        st.subheader("Pull Requests Created")
        st.dataframe(pull_requests)

        st.subheader("Starred Repositories")
        st.dataframe(starred_repos)

        st.subheader("Followers")
        st.dataframe(followers)

        st.subheader("Following")
        st.dataframe(following)

        st.subheader("Gists")
        st.dataframe(gists)

        st.subheader("Organizations")
        st.dataframe(orgs)
    else:
        st.sidebar.warning("Please enter a GitHub username.")

else:
    st.write("Enter a GitHub username in the sidebar and click 'Fetch Data' to explore their activity on GitHub.")
