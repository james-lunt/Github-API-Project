from django.shortcuts import render
from github import Github

# Create your views here.
from django.http import HttpResponse

#access token = personal access token from https://github.com/settings/tokens
#using access token
g = Github("Access Token")
repo_list = []
for repo in g.get_user().get_repos():
        repo_list.append(repo)

repo1 = repo_list[len(repo_list)-1].name
repo2 = repo_list[len(repo_list)-2].name
repo3 = repo_list[len(repo_list)-3].name
repo4 = repo_list[len(repo_list)-4].name
repo5 = repo_list[len(repo_list)-5].name

#Get commits to a repo
commit_amount_list = []
for repo in repo_list:
        commit_list = []
        for commit in repo.get_commits():
                commit_list.append(commit)
        commit_amount_list.append(len(commit_list))

repoCommit1  = commit_amount_list[0]
repoCommit2  = commit_amount_list[1]
repoCommit3  = commit_amount_list[2]
repoCommit4  = commit_amount_list[3]
repoCommit5  = commit_amount_list[4]


#Get contributors to a repo
contributor_amount_list = []
for repo in repo_list:
        contributor_list = []
        for contributor in repo.get_contributors():
                contributor_list.append(contributor)
        contributor_amount_list.append(len(contributor_list))

repoContrib1 = contributor_amount_list[0]
repoContrib2 = contributor_amount_list[1]
repoContrib3 = contributor_amount_list[2]
repoContrib4 = contributor_amount_list[3]
repoContrib5 = contributor_amount_list[4]

#Get pull requests to a repo
pr_amount_list = []
for repo in repo_list:
        pr_list = []
        for pr in repo.get_pulls():
                pr_list.append(pr)
        pr_amount_list.append(len(pr_list))

repoPr1 = pr_amount_list[0]
repoPr2 = pr_amount_list[1]
repoPr3 = pr_amount_list[2]
repoPr4 = pr_amount_list[3]
repoPr5 = pr_amount_list[4]


def index(request):
    return render(request, 'index.html', {'repo1' : repo1, 'repo2' : repo2, 'repo3' : repo3, 'repo4' : repo4, 'repo5' : repo5,
                                           'repoCommit1' : repoCommit1, 'repoCommit2' : repoCommit2, 'repoCommit3' : repoCommit3, 'repoCommit4' : repoCommit4, 'repoCommit5' : repoCommit5,
                                           'repoContrib1' : repoContrib1, 'repoContrib2' : repoContrib2, 'repoContrib3' : repoContrib3, 'repoContrib4' : repoContrib4, 'repoContrib5' : repoContrib5,
                                           'repoPr1' : repoPr1, 'repoPr2' : repoPr2, 'repoPr3' : repoPr3, 'repoPr4' : repoPr4, 'repoPr5' : repoPr5})
