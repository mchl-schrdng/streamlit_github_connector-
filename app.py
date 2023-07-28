import streamlit as st
from src.github_connector import GitHubConnection
from collections import Counter

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
        st.bar_chart([repo['stargazers_count'] for repo in repos_sorted])

    # Recent Activity
    if st.sidebar.button('📅 Fetch Recent Activity'):
        activity = conn.get_user_activity(github_username)
        st.subheader("Recent Activity")
        st.dataframe(activity)

        # Visualization: Activity Type Distribution
        activity_types = [event['type'] for event in activity]
        activity_count = Counter(activity_types)
        st.bar_chart(activity_count)

        # Visualization: Activity Over Time
        activity_dates = [event['created_at'] for event in activity]
        activity_dates_count = Counter(activity_dates)
        st.line_chart(activity_dates_count)

    # ... [Rest of the code remains similar]

else:
    st.sidebar.warning("Please enter a GitHub username.")
    st.write("Enter a GitHub username in the sidebar and click on the desired data category to explore their activity on GitHub.")
