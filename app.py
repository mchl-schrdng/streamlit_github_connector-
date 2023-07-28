import streamlit as st
from src.github_connector import GitHubConnection

# Create an instance of the GitHubConnection
conn = GitHubConnection("github")

st.set_page_config(layout='wide')

# Sidebar
st.sidebar.image("github-logo.png", width=100)
st.sidebar.title("GitHub User Explorer 🚀")
github_username = st.sidebar.text_input("Enter GitHub Username:")

# Create two columns
col1, col2 = st.columns(2)

if github_username:

    # Profile Information in Column 1
    with col1:
        profile = conn.get_user_profile(github_username)
        st.image(profile['avatar_url'], width=100)
        
        # Relevant Profile Details
        st.write("### 📌 Profile Details")
        st.write("**Username:**", profile['login'])
        st.write("**Name:**", profile['name'] if profile['name'] else "Not provided")
        st.write("**Bio:**", profile['bio'] if profile['bio'] else "Not provided")
        st.write("**Location:**", profile['location'] if profile['location'] else "Not provided")
        st.write("**Profile URL:**", f"[{profile['html_url']}]({profile['html_url']})")
        st.write("**Followers:**", profile['followers'])
        st.write("**Following:**", profile['following'])
        st.write("**Public Repositories:**", profile['public_repos'])
        st.write("**Public Gists:**", profile['public_gists'])
        st.write("**Account Created On:**", profile['created_at'])
        st.write("**Last Updated On:**", profile['updated_at'])
        
        st.dataframe(profile)
        st.json(profile,expanded=False)

    
    # Repositories in Column 2
    with col2:
        if st.sidebar.button('📂 Fetch Repositories'):
            repos = conn.get_user_repositories(github_username)
            st.subheader("📂 Repositories")
            st.dataframe(repos)
            st.json(repos,expanded=False)

        # Recent Activity
        if st.sidebar.button('📅 Fetch Recent Activity'):
            activity = conn.get_user_activity(github_username)
            st.subheader("📅 Recent Activity")
            st.dataframe(activity)
            st.json(activity,expanded=False)
        
        # Issues
        if st.sidebar.button('🐞 Fetch Issues'):
            issues = conn.get_user_issues(github_username)
            st.subheader("🐞 Issues Created")
            st.dataframe(issues)
            st.json(issues,expanded=False)

        # Pull Requests
        if st.sidebar.button('🔄 Fetch Pull Requests'):
            pull_requests = conn.get_user_pull_requests(github_username)
            st.subheader("🔄 Pull Requests Created")
            st.dataframe(pull_requests)
            st.json(pull_requests,expanded=False)

        # Starred Repositories
        if st.sidebar.button('⭐ Fetch Starred Repos'):
            starred_repos = conn.get_user_starred_repos(github_username)
            st.subheader("⭐ Starred Repositories")
            st.dataframe(starred_repos)
            st.json(starred_repos,expanded=False)

        # Followers
        if st.sidebar.button('👥 Fetch Followers'):
            followers = conn.get_user_followers(github_username)
            st.subheader("👥 Followers")
            st.dataframe(followers)
            st.json(followers,expanded=False)

        # Following
        if st.sidebar.button('👣 Fetch Following'):
            following = conn.get_user_following(github_username)
            st.subheader("👣 Following")
            st.dataframe(following)
            st.json(following,expanded=False)

        # Gists
        if st.sidebar.button('📜 Fetch Gists'):
            gists = conn.get_user_gists(github_username)
            st.subheader("📜 Gists")
            st.dataframe(gists)
            st.json(gists,expanded=False)

        # Organizations
        if st.sidebar.button('🏢 Fetch Organizations'):
            orgs = conn.get_user_organizations(github_username)
            st.subheader("🏢 Organizations")
            st.dataframe(orgs)
            st.json(orgs,expanded=False)

else:
    st.sidebar.warning("Please enter a GitHub username.")
    st.write("Enter a GitHub username in the sidebar and click on the desired data category to explore their activity on GitHub.")
