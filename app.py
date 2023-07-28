import streamlit as st
from src.github_connector import GitHubConnection
import pandas as pd

# Create an instance of the GitHubConnection
conn = GitHubConnection("github")

# Sidebar
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
            st.subheader("Repositories")
            st.dataframe(repos)
            st.json(repos,expanded=False)

        # Recent Activity
        if st.sidebar.button('📅 Fetch Recent Activity'):
            activity = conn.get_user_activity(github_username)
            st.subheader("Recent Activity")
            st.dataframe(activity)
            st.json(activity,expanded=False)
            
            # Convert the activity list to a DataFrame
            df_activity = pd.DataFrame(activity)
            
            # Extract date from 'created_at' and count activities by day
            df_activity['date'] = pd.to_datetime(df_activity['created_at']).dt.date
            activity_by_day = df_activity.groupby('date').size().reset_index(name='count')
            
            # Fill missing dates with zero activity
            all_dates = pd.date_range(start=df_activity['date'].min(), end=df_activity['date'].max(), freq='D')
            activity_by_day = activity_by_day.set_index('date').reindex(all_dates).fillna(0).reset_index()
            activity_by_day.columns = ['date', 'count']

            # Display the DataFrame used for the graph
            st.write("Data used for the graph:")
            st.dataframe(activity_by_day)
            
            # Line Graph for Activity by Day
            st.line_chart(activity_by_day.set_index('date'), use_container_width=True)
        
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
