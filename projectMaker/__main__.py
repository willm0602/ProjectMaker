import time
import os, sys
import docx
import subprocess
from trello import TrelloClient 
from github import Github

#goes into project folder
os.chdir("projects")
#gets project name and type from user
projName = input("What is the project name?")
projType = input("What is the type of project?")
if '-1' in projType: #allows the user to cancel if they enter the wrong project name
    sys.exit()

print("moving directory to project") 
os.mkdir(projName)
os.chdir(projName)

#creates "main" script files
print('creating main files')
if 'python' in projType:
    file = open("__main__.py","x")
    file.close()
elif 'node' in projType or 'js' in projType or 'javascript' in projType:
    file = open("main.js","x")
    file.close()
os.chdir("..")
os.chdir("..")
print('main files created')

#connects the user to trello
print('creating Trello sheet')
client = TrelloClient(
    api_key='PUT API KEY FOR TRELLO HERE',
    api_secret='PUT API SECRET FOR TRELLO HERE',
    token='PUT TRELLO CLIENT TOKEN HERE'
)
#creates a trello sheet
client.add_board(projName)
print("Trello added")

#creates a project document
print('creating a project document')
doc = docx.Document("template.docx")
os.chdir("projects")
os.chdir(projName)
doc.save("project.docx")
print('created project document')

#creates a github repository
print("creating github repository")
git = Github("PUT GITHUB CLIENT KEY HERE")
me = git.get_user()
me.create_repo(projName)
print("Github repository created")
print("Project created") #lets the user know the project is ready
