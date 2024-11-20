from backend.app.init_app import create_app, init_routers

app = create_app()
init_routers(app_=app)
