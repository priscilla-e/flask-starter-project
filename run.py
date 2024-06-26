import os
from app import create_app
from waitress import serve

app = create_app()

if __name__ == '__main__':
    host = os.environ.get('HOST') or '0.0.0.0'
    port = os.environ.get('PORT') or 5000

    if os.environ.get("FLASK_ENV", "development") == "production":
        serve(app, host=host, port=port)
    else:
        app.run(host=host, port=port, debug=True)