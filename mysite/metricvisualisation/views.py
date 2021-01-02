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
        recent_repos = [repo_list[len(repo_list)-1], repo_list[len(repo_list)-2], repo_list[len(repo_list)-3], repo_list[len(repo_list)-4], repo_list[len(repo_list)-5] ]
        return recent_repos

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
def getBranches(repo_list):
        branch_amount_list = []
        for repo in repo_list:
                  branch_list = []
                  for branch in repo.get_branches():
                         branch_list.append(branch)
                  branch_amount_list.append(len(branch_list))
        return branch_amount_list



def index(request):
    #call github access functions
    user = "james-lunt"
    repo_list = getRepos("james-lunt")
    commit_amount_list = getCommits(repo_list)
    contributor_amount_list = getContribs(repo_list)
    branch_amount_list = getBranches(repo_list)

    return render(
        request,
        'index.html',
        {
        'person':user,
        
        'repo1':repo_list[0].name,
        'repo2':repo_list[1].name,
        'repo3':repo_list[2].name,
        'repo4':repo_list[3].name,
        'repo5':repo_list[4].name,

        'repoCommit1':commit_amount_list[0],
        'repoCommit2':commit_amount_list[1],
        'repoCommit3':commit_amount_list[2],
        'repoCommit4':commit_amount_list[3],
        'repoCommit5':commit_amount_list[4],

        'repoContrib1':contributor_amount_list[0],
        'repoContrib2':contributor_amount_list[1],
        'repoContrib3':contributor_amount_list[2],
        'repoContrib4':contributor_amount_list[3],
        'repoContrib5':contributor_amount_list[4],

        'repoBranch1':branch_amount_list[0],
        'repoBranch2':branch_amount_list[1],
        'repoBranch3':branch_amount_list[2],
        'repoBranch4':branch_amount_list[3],
        'repoBranch5':branch_amount_list[4]
        }
    )

def find(request):
  
    user = request.GET['search']

    try:
        repo_list = getRepos(user)
        commit_amount_list = getCommits(repo_list)
        contributor_amount_list = getContribs(repo_list)
        branch_amount_list = getBranches(repo_list)
        
        return render(
                request,
                'index.html',
                {
                'person':user,
                
                'repo1':repo_list[0].name,
                'repo2':repo_list[1].name,
                'repo3':repo_list[2].name,
                'repo4':repo_list[3].name,
                'repo5':repo_list[4].name,

                'repoCommit1':commit_amount_list[0],
                'repoCommit2':commit_amount_list[1],
                'repoCommit3':commit_amount_list[2],
                'repoCommit4':commit_amount_list[3],
                'repoCommit5':commit_amount_list[4],

                'repoContrib1':contributor_amount_list[0],
                'repoContrib2':contributor_amount_list[1],
                'repoContrib3':contributor_amount_list[2],
                'repoContrib4':contributor_amount_list[3],
                'repoContrib5':contributor_amount_list[4],

                'repoBranch1':branch_amount_list[0],
                'repoBranch2':branch_amount_list[1],
                'repoBranch3':branch_amount_list[2],
                'repoBranch4':branch_amount_list[3],
                'repoBranch5':branch_amount_list[4]
                }
        )
    except:
           return render(request,'find.html')
