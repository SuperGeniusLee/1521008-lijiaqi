
from BigHomework import create_app, db

app = create_app()

if __name__ == '__main__':
    app.run(debug = True, port = 8080)
    # pass
