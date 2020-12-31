from django.shortcuts import render
from github import Github
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure

# Create your views here.
from django.http import HttpResponse

#access token = personal access token from https://github.com/settings/tokens
#using access token
g = Github("AccessToken")
repo_list = []
for repo in g.get_user().get_repos():
        repo_list.append(repo)

repo1 = repo_list[0].name
repo2 = repo_list[1].name
repo3 = repo_list[2].name
repo4 = repo_list[3].name
repo5 = repo_list[4].name

#Get commits to a repo
commit_amount_list = []
for repo in repo_list:
        commit_list = []
        for commit in repo.get_commits():
                commit_list.append(commit)
        commit_amount_list.append(len(commit_list))


#Get contributors to a repo
contributor_amount_list = []
for repo in repo_list:
        contributor_list = []
        for contributor in repo.get_contributors():
                contributor_list.append(contributor)
        contributor_amount_list.append(len(contributor_list))


#Get pull requests to a repo
pr_amount_list = []
for repo in repo_list:
        pr_list = []
        for pr in repo.get_pulls():
                pr_list.append(pr)
        pr_amount_list.append(len(pr_list))


def index(request):
    fig = Figure()

    # draw your plot here ......
    labels = [repo_list[0].name, repo_list[1].name, repo_list[2].name, repo_list[3].name, repo_list[4].name]

    repo_commits = [commit_amount_list[0], commit_amount_list[1], commit_amount_list[2], commit_amount_list[3], commit_amount_list[4]]
    repo_contribs = [contributor_amount_list[0], contributor_amount_list[1], contributor_amount_list[2], contributor_amount_list[3], contributor_amount_list[4]]
    repo_pr = [pr_amount_list[0], pr_amount_list[1], pr_amount_list[2], pr_amount_list[3], pr_amount_list[4]]

    x = np.arange(len(labels))  # the label locations
    width = 0.15  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x, repo_commits, width, label='Commits')
    rects2 = ax.bar(x + width, repo_contribs, width, label='Contributions')
    rects3 = ax.bar(x - width, repo_pr, width, label='Pull Request')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_title('Scores by group and gender')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    #rotate labels so theyre readable
    plt.xticks(rotation=45)


    def autolabel(rects):
    
     for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


    autolabel(rects1)
    autolabel(rects2)

    fig.tight_layout()
    

    canvas = FigureCanvasAgg(fig)
    response = HttpResponse(content_type = 'image/png')
    canvas.print_png(response)
    return response

    #return render(request, 'index.html', {'repo1' : repo1, 'repo2' : repo2, 'repo3' : repo3, 'repo4' : repo4, 'repo5' : repo5,
     #                                      'repoCommit1' : repoCommit1, 'repoCommit2' : repoCommit2, 'repoCommit3' : repoCommit3, 'repoCommit4' : repoCommit4, 'repoCommit5' : repoCommit5,
      #                                     'repoContrib1' : repoContrib1, 'repoContrib2' : repoContrib2, 'repoContrib3' : repoContrib3, 'repoContrib4' : repoContrib4, 'repoContrib5' : repoContrib5,
       #                                    'repoPr1' : repoPr1, 'repoPr2' : repoPr2, 'repoPr3' : repoPr3, 'repoPr4' : repoPr4, 'repoPr5' : repoPr5})
