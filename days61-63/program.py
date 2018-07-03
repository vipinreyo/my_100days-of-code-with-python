from dotenv import load_dotenv, find_dotenv
from github import Github, InputFileContent
import os

load_dotenv(find_dotenv())

code = '''
from github import Github
from collections import namedtuple

Repo = namedtuple('Repo', 'name, stars, forks')

def get_github_repos(name):
    repos = []
    gh = Github()
    nu = gh.get_user(name)
    
    for repo in nu.get_repos():
        if repo.fork:
            continue
            
        repos.append(Repo(name=repo.name, stars=repo.stargazers_count, forks=repo.forks))
    
    return repos
'''


def main():
    token = os.getenv('GIT_HUB_GIST_EXERCICSE_TOKEN')
    gh = Github(token)
    me = gh.get_user()
    print(me.create_gist(True, {"repos_stats.py": InputFileContent(code)}, "Get Github users repos and stats"))


if __name__ == '__main__':
    main()
