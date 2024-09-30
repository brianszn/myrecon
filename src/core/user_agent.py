import requests
from random import choice

def req(url) -> str:

    with open('src/core/user-agents.txt', 'r') as f:
        user_agents: str = f.readlines()
        user_agent: str = choice(user_agents).strip()

    headers = {
        'User-Agent': user_agent
    }

    response = requests.get(url, headers=headers)

    print(user_agent)
    return response
    
