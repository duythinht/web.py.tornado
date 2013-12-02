from pi.route import Route

# Handle site urls
Route.handle('/', 'app.index.Greeting')

# Handle API urls
Route.handle_api('/hello', 'app.api.Greeting')

# Dispatch
urls = Route.urls()
