from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! My Python app is running on Azure Web App 🚀"

if __name__ == "__main__":
    app.run()