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

newcontent = filecontent.replace("Andrew", input("Please enter your name: "))
gitHubResponse=repo.update_file(fileinfo.path,"updated by prog",newcontent,fileinfo.sha)
print(gitHubResponse)











