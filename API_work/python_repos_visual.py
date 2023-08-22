from python_repos import Github_repos

from plotly.graph_objs import Bar
from plotly import offline

repos_urls, repos_stars, labels = [],[],[]

response = Github_repos().get_repos()

for reposit in response:
    name = reposit['name']
    url = reposit['html_url']
    repos_url = f"<a href='{url}'>{name}</a>"
    repos_urls.append(repos_url)
    repos_stars.append(reposit['stargazers_count'])

    owner = reposit['owner']['login']
    description = reposit['description']
    label = f"{owner} <br /> {description}"
    labels.append(label)

data = [{
    "type" : 'bar',
    "x" : repos_urls,
    "y" : repos_stars,
    "hovertext" : labels,
    "marker" : {
        "color" : "rgb(100,40,120)",
        "line" : {"width" : 3, "color" : "rgb(120,40,100)"}
    },
    "opacity" : 0.8,
}]

my_layout = {
    "title" : "Most starred Python projects on GitHub in 2023",
    "xaxis" : {
        "title" : "Repositories",
        "titlefont" : {"size" : 24},
        "tickfont" : {"size" : 14},
        },
    "yaxis" : {
        "title" : "Star count",
        "titlefont" : {"size" : 24},
        "tickfont" : {"size" : 14},
        },
}

fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig,filename="python_repos_statistic.html")