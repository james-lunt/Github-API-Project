from github import Github

#using access token
g = Github("Access Token")

for repo in g.get_user().get_repos():
    print(repo.name)
