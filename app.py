from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return "id_list_message=t-השלוחה עובדת"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
