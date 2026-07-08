from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Flask!",
        "status": "success"
    })

@app.route("/about")
def about():
    return jsonify({
        "application": "Flask Sample App",
        "developer": "Divya Bhamare",
        "language": "Python",
        "framework": "Flask"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

if __name__ == "__main__":
    app.run(debug=True)