from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>SIT223 DevOps Application</h1>
    <p>Jenkins CI/CD Pipeline Demo</p>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "SIT223 DevOps Application"
    })


@app.route("/api/message")
def message():
    return jsonify({
        "message": "Hello from the SIT223 Jenkins Pipeline!"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
