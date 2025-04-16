import requests #needed to make HTTP requests
from github import Github #allows me to interact with the Github API
from config import config as cfg #my configuration file containing my github key

apikey = cfg['githubkey']
g = Github(apikey) # in these 2 lines, I'm retrieving my key from the config file and authenticating myself

repo = g.get_repo("MylesHenehan/privaterepo") # here, now I've authenticated myself, I can access my private repo

fileinfo = repo.get_contents("andrew.txt")
# print(fileinfo) - used to check the info about the file, including commit history
fileurl = fileinfo.download_url

response = requests.get(fileurl) # the get request retrieves the raw content from the file, while .text converts this to a string.
filecontent = response.text
print(filecontent)

if "Andrew" in filecontent:
    newcontent = filecontent.replace("Andrew", input("Please enter your name: ")) # now I can replace the instances of "Andrew" in the file with whatever the user's name is.
    gitHubResponse=repo.update_file(fileinfo.path,"updated by prog",newcontent,fileinfo.sha) # finally, I commit this to Github
    print(gitHubResponse)
else:
    print("The file does not contain the string 'Andrew'. There are no changes to be made.")











