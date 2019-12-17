import json
import requests

def auto_login(view, *args, **kwargs):
    def decorator(self, *args, **kwargs):
        if (self.token == None):
            resp = requests.post(
                f'{self.api_url}/login',
                json={
                    'username': self.username,
                    'password': self.password
                }
            ).text
            self.token = json.loads(resp)['access_token']
        return view(self, *args, **kwargs)
    return decorator
