from github import Github

#using access token
g = Github("60b44c78e988ba34fdb880f9fbad5d9d106b23b5")

#find hololens project
for repo in g.get_user().get_repos():
        myRepo = repo
        print(repo)

print(myRepo.name)

#Get commits to a repo
commits = myRepo.get_commits()
commits_sha_list = []
for commit in commits:
    print (commit.url)