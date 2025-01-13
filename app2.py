from markupsafe import escape
from flask import Flask

app2 = Flask(__name__)

@app2.route("/<name>")
def Hello(name):
    return f"Hello, {escape(name)}!"

if __name__ == "__main__":
    app2.run(debug=True,port=5001)
