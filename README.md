# Streamlit GitHub Explorer 🚀

Streamlit GitHub Explorer is a web application that allows users to explore and visualize the activity of any GitHub user. By simply entering a GitHub username, you can retrieve and visualize various details like profile information, repositories, recent activity, and more.

## Features 🌟

- **Profile Overview**: Get a quick glance at a user's profile, including their avatar, bio, location, followers count, and more.
  
- **Repositories**: View the list of repositories owned by the user.
  
- **Recent Activity**: Visualize the user's recent activity on GitHub, including a line chart showing activity by day and a donut chart showing the distribution of activity types.
  
- **Issues & Pull Requests**: See the issues raised and pull requests made by the user.
  
- **Starred Repositories**: Discover the repositories that the user has starred.
  
- **Followers & Following**: Check out who the user is following and who follows them.
  
- **Gists**: Browse through the gists created by the user.
  
- **Organizations**: Find out the organizations the user is a part of.

## Connector and ExperimentalBaseConnection 🌐

The application uses a custom connector built on top of Streamlit's `ExperimentalBaseConnection`. This connector interfaces with the GitHub API to fetch the required data. The use of `ExperimentalBaseConnection` allows for a more modular and scalable approach, enabling easy integration with various data sources and APIs.

## Built With 🛠️

- **Streamlit**: The core framework used to build the web application.
  
- **GitHub API**: Used to fetch all the data related to GitHub users.

## Usage 💡

1. Navigate to the Streamlit GitHub Explorer web application.
  
2. Enter a GitHub username in the sidebar.
  
3. Click on the desired data category buttons to explore the user's activity on GitHub.
