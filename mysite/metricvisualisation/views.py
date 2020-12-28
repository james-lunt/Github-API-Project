from django.shortcuts import render
from github import Github

# Create your views here.
from django.http import HttpResponse

#access token = personal access token from https://github.com/settings/tokens
#using access token
g = Github("Github Access token")

#find hololens project
repo_list = []
for repo in g.get_user().get_repos():
        repo_list.append(repo.name)

repo1 = repo_list[0]
repo2 = repo_list[1]
repo3 = repo_list[2]
repo4 = repo_list[3]

def index(request):
    return render(request, 'index.html', {'repo1' : repo1, 'repo2' : repo2, 'repo3' : repo3, 'repo4' : repo4})
