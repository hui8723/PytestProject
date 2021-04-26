import requests

class RestApi():

    def __init__(self, url, key, value, method):
        self.url = url
        self.key = key
        self.value = value
        self.method = method

    def run(self):
        response = requests.request(self.method, self.url)
        return response