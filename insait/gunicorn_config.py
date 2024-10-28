from insait.server import setup_app

bind = "0.0.0.0:5000"


def post_fork(server, worker):
    setup_app()
