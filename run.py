import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    host = os.environ.get('HOST') or '0.0.0.0'
    port = os.environ.get('PORT') or 5000
    app.run(host=host, port=port, debug=True)