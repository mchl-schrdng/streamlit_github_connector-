import streamlit as st
from src.github_connector import GitHubConnection

# Create an instance of the GitHubConnection
conn = GitHubConnection("github")

# Sidebar
st.sidebar.title("GitHub User Explorer 🚀")
github_username = st.sidebar.text_input("Enter GitHub Username:")

if github_username:

    if st.sidebar.button('🧑 Fetch Profile'):
        profile = conn.get_user_profile(github_username)
        st.subheader(f"Profile of {github_username}")
        st.dataframe(profile)

    if st.sidebar.button('📅 Fetch Recent Activity'):
        activity = conn.get_user_activity(github_username)
        st.subheader("Recent Activity")
        st.dataframe(activity)

    if st.sidebar.button('📂 Fetch Repositories'):
        repos = conn.get_user_repositories(github_username)
        st.subheader("Repositories")
        st.dataframe(repos)

    if st.sidebar.button('🐞 Fetch Issues'):
        issues = conn.get_user_issues(github_username)
        st.subheader("Issues Created")
        st.dataframe(issues)

    if st.sidebar.button('🔄 Fetch Pull Requests'):
        pull_requests = conn.get_user_pull_requests(github_username)
        st.subheader("Pull Requests Created")
        st.dataframe(pull_requests)

    if st.sidebar.button('⭐ Fetch Starred Repos'):
        starred_repos = conn.get_user_starred_repos(github_username)
        st.subheader("Starred Repositories")
        st.dataframe(starred_repos)

    if st.sidebar.button('👥 Fetch Followers'):
        followers = conn.get_user_followers(github_username)
        st.subheader("Followers")
        st.dataframe(followers)

    if st.sidebar.button('👣 Fetch Following'):
        following = conn.get_user_following(github_username)
        st.subheader("Following")
        st.dataframe(following)

    if st.sidebar.button('📜 Fetch Gists'):
        gists = conn.get_user_gists(github_username)
        st.subheader("Gists")
        st.dataframe(gists)

    if st.sidebar.button('🏢 Fetch Organizations'):
        orgs = conn.get_user_organizations(github_username)
        st.subheader("Organizations")
        st.dataframe(orgs)

else:
    st.sidebar.warning("Please enter a GitHub username.")
    st.write("Enter a GitHub username in the sidebar and click on the desired data category to explore their activity on GitHub.")
