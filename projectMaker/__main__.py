import time
import os, sys
import docx
import subprocess
from trello import TrelloClient 
from github import Github

os.chdir("projects")
projName = input("What is the project name?")
projType = input("What is the type of project?")
if '-1' in projType:
    sys.exit()
print("moving directory to project")
os.mkdir(projName)
os.chdir(projName)
print('creating main files')
if 'python' in projType:
    file = open("__main__.py","x")
    file.close()
elif 'node' in projType or 'js' in projType or 'javascript' in projType:
    file = open("main.js","x")
    file.close()
print('main file created')
os.chdir("..")
os.chdir("..")
print('creating Trello sheet')
client = TrelloClient(
    api_key='9845e03120568ee8d508627604860b63',
    api_secret='add3d4717a145157157e9e403b9c9195e8f5d4e504e6bbb4e71f55b6b52dc186',
    token='0260507a99b5cee419cd8ccf1f6aae21483e2733a3f57b9a788515138f05da02'
)
client.add_board(projName)
print("Trello added")

print('creating a project document')
doc = docx.Document("template.docx")
os.chdir("projects")
os.chdir(projName)
doc.save("project.docx")
print('created project document')

print("creating github repository")
git = Github("0aabc66d3372dff4ee384229c357b5341060e1e8")
me = git.get_user()
me.create_repo(projName)
print("Github repository created")
print("Project created")