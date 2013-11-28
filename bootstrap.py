import web
from routes import urls

app = web.application(urls, globals())
application = app.wsgifunc()

if __name__ == '__main__':
    app.run()
