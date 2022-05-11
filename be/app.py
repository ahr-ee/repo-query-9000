import asyncio
from uuid import uuid4


import asyncio
import requests
from uuid import uuid4

MAX_EL = 5

class BigApp:
    def __init__(self):
        print("hello world")
        self.clients = {}

    def process_request(self, request):
        username = request
        r = requests.get(f"https://api.github.com/users/{username}/repos")
        try:
            info_list = parse_curl(r.json())
            self.respond({username: info_list})
        except:
            self.respond("BAD REQUEST")

    def respond(self, response, client_id = None):
        clients = [self.clients[client_id]] if client_id else self.clients.values()
        for client in clients:
            asyncio.create_task(client(response))

    def register_client(self, client_callback):
        client_id = str(uuid4())
        self.clients[client_id] = client_callback
        return client_id

    def unregister_client(self, client_id: str):
        del self.clients[client_id]

def parse_curl(curl_blob):
    el_count = 0
    info_list = []
    for el in curl_blob:
        if el_count >= MAX_EL:
            break
        info_list.append({
                "name": el["name"],
                "html_url": el["html_url"],
                "description": el["description"],
                "language": el["language"],
            }
        )
        el_count += 1
    return info_list
