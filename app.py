
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    """Return the application's homepage."""
    return """
    <h1>SIT223 DevOps Application</h1>
    <p>Jenkins CI/CD Pipeline Demo</p>
    """


@app.route("/health")
def health():
    """Return the application's health status."""
    return jsonify({
        "status": "healthy",
        "service": "SIT223 DevOps Application"
    })


@app.route("/api/message")
def message():
    """Return a sample API message."""
    return jsonify({
        "message": "Hello from the SIT223 Jenkins Pipeline!"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
