from waitress import serve
from app.app import create_app

my_app = create_app()

if __name__ == '__main__':
    serve(my_app, host="localhost", port=5000)

