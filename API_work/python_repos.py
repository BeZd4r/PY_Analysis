import requests

class Github_repos:
    
    def __init__(self):
        
        self.url = "https://api.github.com/search/repositories?"
        self.params = {"q" : "language:python","sort" : "stars"}
        self.headers = {"Accept": "application/vnd.github.v3+json"}
        

    def get_repos(self,lang = "python", srt = "stars"):
        self.params = {"q" : f"language:{lang}", "sort" : srt}

        response = requests.get(self.url,headers=self.headers,params=self.params)
        if response.status_code == 200:
            return response.json()['items']
        else:
            print(f"Error {response['status_code']}")
        

