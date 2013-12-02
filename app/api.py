from json import dumps
from config import api_version

class Greeting:
    def GET(self):
        return dumps({'message': 'Hello, World!', 'version': api_version})
