from django.shortcuts import render
from github import Github

# Create your views here.
from django.http import HttpResponse

#access token = personal access token from https://github.com/settings/tokens
#using access token
g = Github("")

#get repos
def getRepos(user):
        repo_list = []
        for repo in g.get_user(user).get_repos():
            repo_list.append(repo)
        return repo_list


#Get commits to a repo
def getCommits(repo_list):
        commit_amount_list = []
        for repo in repo_list:
                commit_list = []
                for commit in repo.get_commits():
                     commit_list.append(commit)
                commit_amount_list.append(len(commit_list))
        return commit_amount_list


#Get contributors to a repo
def getContribs(repo_list):
        contributor_amount_list = []
        for repo in repo_list:
                 contributor_list = []
                 for contributor in repo.get_contributors():
                         contributor_list.append(contributor)
                 contributor_amount_list.append(len(contributor_list))
        return contributor_amount_list


#Get pull requests to a repo
def getPr(repo_list):
        pr_amount_list = []
        for repo in repo_list:
                  pr_list = []
                  for pr in repo.get_pulls():
                         pr_list.append(pr)
                  pr_amount_list.append(len(pr_list))
        return pr_amount_list



def index(request):
    #call github access functions
    user = "james-lunt"
    repo_list = getRepos("james-lunt")
    commit_amount_list = getCommits(repo_list)
    contributor_amount_list = getContribs(repo_list)
    pr_amount_list = getPr(repo_list)
   
    #parse date to be visualise
    repo1 = repo_list[len(repo_list)-1].name
    repo2 = repo_list[len(repo_list)-2].name
    repo3 = repo_list[len(repo_list)-3].name
    repo4 = repo_list[len(repo_list)-4].name
    repo5 = repo_list[len(repo_list)-5].name

    repoCommit1  = commit_amount_list[len(commit_amount_list)-1]
    repoCommit2  = commit_amount_list[len(commit_amount_list)-2]
    repoCommit3  = commit_amount_list[len(commit_amount_list)-3]
    repoCommit4  = commit_amount_list[len(commit_amount_list)-4]
    repoCommit5  = commit_amount_list[len(commit_amount_list)-5]

    repoContrib1 = contributor_amount_list[len(contributor_amount_list)-1]
    repoContrib2 = contributor_amount_list[len(contributor_amount_list)-2]
    repoContrib3 = contributor_amount_list[len(contributor_amount_list)-3]
    repoContrib4 = contributor_amount_list[len(contributor_amount_list)-4]
    repoContrib5 = contributor_amount_list[len(contributor_amount_list)-5]

    repoPr1 = pr_amount_list[len(pr_amount_list)-1]
    repoPr2 = pr_amount_list[len(pr_amount_list)-2]
    repoPr3 = pr_amount_list[len(pr_amount_list)-3]
    repoPr4 = pr_amount_list[len(pr_amount_list)-4]
    repoPr5 = pr_amount_list[len(pr_amount_list)-5]


    return render(request, 'index.html', {'person' : user, 'repo1' : repo1, 'repo2' : repo2, 'repo3' : repo3, 'repo4' : repo4, 'repo5' : repo5,
                                           'repoCommit1' : repoCommit1, 'repoCommit2' : repoCommit2, 'repoCommit3' : repoCommit3, 'repoCommit4' : repoCommit4, 'repoCommit5' : repoCommit5,
                                           'repoContrib1' : repoContrib1, 'repoContrib2' : repoContrib2, 'repoContrib3' : repoContrib3, 'repoContrib4' : repoContrib4, 'repoContrib5' : repoContrib5,
                                           'repoPr1' : repoPr1, 'repoPr2' : repoPr2, 'repoPr3' : repoPr3, 'repoPr4' : repoPr4, 'repoPr5' : repoPr5})

def find(request):
        
    user = request.GET['search']
    repo_list = getRepos(user)
    commit_amount_list = getCommits(repo_list)
    contributor_amount_list = getContribs(repo_list)
    pr_amount_list = getPr(repo_list)
   
    #parse date to be visualise
    repo1 = repo_list[len(repo_list)-1].name
    repo2 = repo_list[len(repo_list)-2].name
    repo3 = repo_list[len(repo_list)-3].name
    repo4 = repo_list[len(repo_list)-4].name
    repo5 = repo_list[len(repo_list)-5].name

    repoCommit1  = commit_amount_list[len(commit_amount_list)-1]
    repoCommit2  = commit_amount_list[len(commit_amount_list)-2]
    repoCommit3  = commit_amount_list[len(commit_amount_list)-3]
    repoCommit4  = commit_amount_list[len(commit_amount_list)-4]
    repoCommit5  = commit_amount_list[len(commit_amount_list)-5]

    repoContrib1 = contributor_amount_list[len(contributor_amount_list)-1]
    repoContrib2 = contributor_amount_list[len(contributor_amount_list)-2]
    repoContrib3 = contributor_amount_list[len(contributor_amount_list)-3]
    repoContrib4 = contributor_amount_list[len(contributor_amount_list)-4]
    repoContrib5 = contributor_amount_list[len(contributor_amount_list)-5]

    repoPr1 = pr_amount_list[len(pr_amount_list)-1]
    repoPr2 = pr_amount_list[len(pr_amount_list)-2]
    repoPr3 = pr_amount_list[len(pr_amount_list)-3]
    repoPr4 = pr_amount_list[len(pr_amount_list)-4]
    repoPr5 = pr_amount_list[len(pr_amount_list)-5]

    return render(request, 'index.html', {'person' : user, 'repo1' : repo1, 'repo2' : repo2, 'repo3' : repo3, 'repo4' : repo4, 'repo5' : repo5,
                                           'repoCommit1' : repoCommit1, 'repoCommit2' : repoCommit2, 'repoCommit3' : repoCommit3, 'repoCommit4' : repoCommit4, 'repoCommit5' : repoCommit5,
                                           'repoContrib1' : repoContrib1, 'repoContrib2' : repoContrib2, 'repoContrib3' : repoContrib3, 'repoContrib4' : repoContrib4, 'repoContrib5' : repoContrib5,
                                           'repoPr1' : repoPr1, 'repoPr2' : repoPr2, 'repoPr3' : repoPr3, 'repoPr4' : repoPr4, 'repoPr5' : repoPr5})
