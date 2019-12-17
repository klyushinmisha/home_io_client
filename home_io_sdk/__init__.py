import json

import requests

from .utils import auto_login

class HomeIoClient:
    api_url = ''

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.token = None

    @auto_login
    def push_log(self, dev_uuid, log, tag):
        resp = requests.post(
            f'{self.api_url}/devices/{dev_uuid}/logs',
            json=[{
                'log': json.dumps(log),
                'tag': tag
            }],
            headers={
                'Authorization': f'Bearer {self.token}'
            }
        ).text


    @auto_login
    def get_tasks(self, dev_uuid):
        resp = requests.get(
            f'{self.api_url}/devices/{dev_uuid}/tasks',
            headers={
                'Authorization': f'Bearer {self.token}'
            }
        ).text

        return list(map(
            lambda task: task['task'],
            json.loads(resp)
        ))