import requests
from github import Github
from config import config as cfg

apikey = cfg['githubkey']
g = Github(apikey)

repo = g.get_repo("MylesHenehan/privaterepo")

fileinfo = repo.get_contents("andrew.txt")
fileurl = fileinfo.download_url

response = requests.get(fileurl)
filecontent = response
print(filecontent)










