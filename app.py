import streamlit as st
from src.github_connector import GitHubConnection

# Create an instance of the GitHubConnection
conn = GitHubConnection("github")

# Sidebar
st.sidebar.title("GitHub User Explorer 🚀")
github_username = st.sidebar.text_input("Enter GitHub Username:")

if github_username:

    # Profile Information
    profile = conn.get_user_profile(github_username)
    st.image(profile['avatar_url'], width=100)
    st.write(f"**Name:** {profile['name']}")
    st.write(f"**Bio:** {profile['bio']}")
    st.write(f"**Location:** {profile['location']}")

    # Repositories
    if st.sidebar.button('📂 Fetch Repositories'):
        repos = conn.get_user_repositories(github_username)
        st.subheader("Repositories")
        st.dataframe(repos)
        # Visualization: Bar chart of top repositories based on stars
        repos_sorted = sorted(repos, key=lambda x: x['stargazers_count'], reverse=True)[:10]
        st.bar_chart([repo['stargazers_count'] for repo in repos_sorted], use_container_width=True)

    # Recent Activity
    if st.sidebar.button('📅 Fetch Recent Activity'):
        activity = conn.get_user_activity(github_username)
        st.subheader("Recent Activity")
        st.dataframe(activity)

    # Issues
    if st.sidebar.button('🐞 Fetch Issues'):
        issues = conn.get_user_issues(github_username)
        st.subheader("Issues Created")
        st.dataframe(issues)

    # Pull Requests
    if st.sidebar.button('🔄 Fetch Pull Requests'):
        pull_requests = conn.get_user_pull_requests(github_username)
        st.subheader("Pull Requests Created")
        st.dataframe(pull_requests)

    # Starred Repositories
    if st.sidebar.button('⭐ Fetch Starred Repos'):
        starred_repos = conn.get_user_starred_repos(github_username)
        st.subheader("Starred Repositories")
        st.dataframe(starred_repos)

    # Followers
    if st.sidebar.button('👥 Fetch Followers'):
        followers = conn.get_user_followers(github_username)
        st.subheader("Followers")
        st.dataframe(followers)

    # Following
    if st.sidebar.button('👣 Fetch Following'):
        following = conn.get_user_following(github_username)
        st.subheader("Following")
        st.dataframe(following)

    # Gists
    if st.sidebar.button('📜 Fetch Gists'):
        gists = conn.get_user_gists(github_username)
        st.subheader("Gists")
        st.dataframe(gists)

    # Organizations
    if st.sidebar.button('🏢 Fetch Organizations'):
        orgs = conn.get_user_organizations(github_username)
        st.subheader("Organizations")
        st.dataframe(orgs)

else:
    st.sidebar.warning("Please enter a GitHub username.")
    st.write("Enter a GitHub username in the sidebar and click on the desired data category to explore their activity on GitHub.")
