from github import Github

#using access token
g = Github("bef06aad3961363a56f1289c401e42d11e74e614")

for repo in g.get_user().get_repos():
    print(repo.name)
    repo.edit(has_wiki=False)
