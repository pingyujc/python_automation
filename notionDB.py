import os
from notion_client import Client
from pprint import pprint



NOTION_TOKEN = 'secret_UE1WhBd9cLlgMnfuQkA7JlJz9VxPAACEOMxyyRgTxJL'
DATABASE_ID = "2ab50e8ff014469a8ec693c5a02bfc32"



def write_row(client, database_id, problem, link):
    #database = client.databases.retrieve(database_id)

    new_page = client.pages.create(
        parent={
            "type": "database_id",
            "database_id": database_id
        },
        properties={
            'Problem': {
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


def main():
    client = Client(auth=NOTION_TOKEN)

    problem = 'First Good Version'
    link = 'https://leetcode.com/problems/first-bad-version/'
    
    write_row(client, DATABASE_ID, problem, link)


if __name__ == '__main__':
    main()
          