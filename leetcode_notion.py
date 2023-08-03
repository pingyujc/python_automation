import requests
from bs4 import BeautifulSoup
import os
from notion_client import Client
from pprint import pprint


# the url of grind75
url = 'https://www.techinterviewhandbook.org/grind75?hours=8&weeks=8'

# get the html contents
html = requests.get(url)

# print(html.text)

# parse the content
s = BeautifulSoup(html.content, 'html.parser')

# filter to get all the titles
titles = s.find_all('a', class_='text-indigo-600 text-base hover:underline')

# for title in titles:
#     print(title.text) # the problem title
#     print(title.get('href')) # the problem link


# #paste html file into a text file
# file_path = "new_file.txt"  

# with open(file_path, "w") as file:
#     file.write(html.text)


NOTION_TOKEN = 'secret_UE1WhBd9cLlgMnfuQkA7JlJz9VxPAACEOMxyyRgTxJL'
DATABASE_ID = "8b7f4818ca424fe7b1421aaa58acddab" # id of the notion page



def write_row(client, database_id, problem, link):
    new_page = client.pages.create(
        parent={
            "type": "database_id",
            "database_id": database_id
        },
        properties={
            'Question': {
                'title': [
                    {
                        'text': {
                            'content': problem,
                            'link': {
                                'url': link
                            }
                        }
                        
                    }
                ]
            }
        }
    )
    print("Row created successfully!")

# notion client
client = Client(auth=NOTION_TOKEN)

problems = []
links = []

for title in titles:

    problem = title.text
    problems.append(problem)
    link = title.get('href')
    links.append(link)

problems.reverse()
links.reverse()
# print(problems)
# print(links)

for problem, link in zip(problems, links):
    write_row(client, DATABASE_ID, problem, link)