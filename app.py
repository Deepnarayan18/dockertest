from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "hello deep!"  # Lowercase aur comma hata diya

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
