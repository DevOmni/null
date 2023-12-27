import config
import os

from dotenv import load_dotenv

from app import create_app, db

load_dotenv()

sio, app = create_app()


if __name__ == '__main__':
    if os.getenv('FLASK_ENV') == 'development' and len(os.listdir(config.basedir)) == 0:
        with app.app_context:
            db.create_all()
    sio.run(app, debug=True, port=8080, host='0.0.0.0', allow_unsafe_werkzeug=True)
