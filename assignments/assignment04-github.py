import requests
import base64
import json
from github import Github
from config import config as cfg

apikey = cfg["githubkey"]
githuburl = "https://api.github.com/repos/MylesHenehan/privaterepo/contents/andrew.txt"
replacementname = input("Please enter your name: ")

g = Github(apikey)

response = requests.get(githuburl, auth=('token', apikey))
content = response.json()

with open(content, "wb") as file:
    file.replace("Andrew",replacementname)







