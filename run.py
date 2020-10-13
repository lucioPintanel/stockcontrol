from api import create_app
import os, config

app = create_app(os.getenv('FLASK_ENV') or 'config.DevelopementConfig')

if __name__ == '__main__':
    app.run()
