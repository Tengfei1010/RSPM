from celery import Celery
from flask import Flask

flask_app = Flask(__name__)
flask_app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379',
    SECRET_KEY='top-secret!'
)


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


celery = make_celery(flask_app)


@flask_app.route('/', methods=['GET'])
def index():
    from rspm.third_library.whatweb.wrapper import WhatWeb

    scanner = WhatWeb()
    result = scanner.scan("https://csdn.net")
    print(result)
    return result


if __name__ == '__main__':
    flask_app.run(debug=True)
