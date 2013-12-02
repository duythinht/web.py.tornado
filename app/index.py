from json import dumps

class Greeting:
    def GET(self):
        return 'Hello, World'

    def POST(self):
        post_data = web.input()
        return dumps(post_data)


