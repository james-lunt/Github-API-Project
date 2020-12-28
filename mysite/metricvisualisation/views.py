from django.shortcuts import render
from github import Github

# Create your views here.
from django.http import HttpResponse

#access token = personal access token from https://github.com/settings/tokens
#using access token
g = Github(Access token)

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

def index(request):
    return HttpResponse(myRepo.name)
