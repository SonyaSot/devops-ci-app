from flask import Flask

app = Flask(__name__)


@app.get("/")
def index():
    return "DevOps CI app\n"


@app.get("/health")
def health():
    return {"status": "ok"}
