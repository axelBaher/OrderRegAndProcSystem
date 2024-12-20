from backend.app.init_app import create_app, init_routers, init_cors

app = create_app()
init_routers(app_=app)
init_cors(app_=app)
