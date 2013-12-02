from config import api_prefix

class Route:
    sites = ()
    apis = ()

    @staticmethod
    def handle(url, handler):
        Route.sites = Route.sites + (url, handler)

    @staticmethod
    def handle_api(url, handler):
        Route.apis = Route.apis + (api_prefix + url, handler)

    @staticmethod
    def urls():
        return Route.sites + Route.apis

