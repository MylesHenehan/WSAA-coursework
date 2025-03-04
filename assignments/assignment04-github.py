import requests
from github import Github
from config import config as cfg

apikey = cfg["githubkey"]
g = Github(apikey)

for repo in g.get_user().get_repos():
 print(repo.name)

repo = g.get_repo("MylesHenehan/privaterepo")
print(repo.clone_url)

fileInfo = repo.get_contents("andrew.txt")
urlOfFile = fileInfo.download_url
print (urlOfFile)

response = requests.get(urlOfFile)
filecontent = response.text
print(filecontent)