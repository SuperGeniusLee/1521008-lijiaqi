from web import create_app, db

app = create_app()


def init():
    init_app = create_app()
    app_context = init_app.app_context()
    app_context.push()
    db.create_all()


if __name__ == '__main__':
    init()
    app.run(debug = True, port = 8080)
