"""Flask application for the DevOps CI practice project."""

from flask import Flask


def create_app():
    """Create a Flask application with the service and health routes."""
    application = Flask(__name__)

    @application.get("/")
    def index():
        return {"service": "devops-ci-app", "version": "1.0.0", "status": "running"}

    @application.get("/health")
    def health():
        return {"status": "ok"}

    return application


app = create_app()
