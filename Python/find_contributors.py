from github import Github

# Replace with your personal access token
# You can generate one at https://github.com/settings/tokens
github_token = "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"

# Replace with the owner and name of the repository
owner = "openvinotoolkit"
repo_name = "openvino"

# Create a GitHub object
g = Github(github_token)

# Get the repository
repo = g.get_repo(f"{owner}/{repo_name}")

# Get all contributors
contributors = list(repo.get_contributors())

# Print contributor names
for contributor in contributors:
  print(contributor.login)
