from os import path
from json import load, dump
import asyncio
import requests
from common import parse_curl
from test_curl import test_curl_array

async def periodic_tasker(interval, func):
    while True:
        await asyncio.gather(
            asyncio.sleep(interval),
            func()
        )

class DbHandler:
    def __init__(self):
        self._file_loc = path.abspath(".\database.json")
        try:
            self._loop = asyncio.get_event_loop()
        except RuntimeError:
            self._loop = asyncio.get_running_loop()


        asyncio.create_task(periodic_tasker(10, self.refresh_db))

    def update_db(self, username, repo_list):
        with open(self._file_loc, "rb") as f:
            file_data = load(f)

        file_data.update({username: repo_list})

        with open(self._file_loc, "w+") as f:
            dump(file_data, f, indent=4, sort_keys=True)

    def check_for_user(self, username):
        with open(self._file_loc, "rb") as f:
            file_data = load(f)
        if username in file_data:
            return True
        return False

    def query_users(self):
        with open(self._file_loc, "rb") as f:
            file_data = load(f)

        return file_data.keys()

    async def refresh_db(self):
        users = self.query_users()
        for user in users:
            r = requests.get(f"https://api.github.com/users/{user}/repos")
            try:
                repo_list = parse_curl(r.json())
                self.update_db(user, repo_list)
            except Exception as e:
                raise RuntimeError("Cannot refresh db") from e

