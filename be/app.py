import asyncio
from uuid import uuid4
from database_handler import DbHandler
import asyncio
import requests
from uuid import uuid4
from common import parse_curl
from test_curl import test_curl_array

class BigApp:
    def __init__(self):
        self._db_handler = DbHandler()
        self.clients = {}

    def process_request(self, request):
        username = request
        r = requests.get(f"https://api.github.com/users/{username}/repos")
        try:
            repo_list = parse_curl(r.json())
            new_username = True
            if(self._db_handler.check_for_user(username)):
                new_username = False
            self._db_handler.update_db(username, repo_list)
            user_dict = {username: {"repos": repo_list, "new_username": new_username}}
            self.respond(user_dict)
        except Exception as e:
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