from json import dumps

class Welcome:
    def GET(self):
        return 'Hello'

    def POST(self):
        post_data = web.input()
        return dumps(post_data)


