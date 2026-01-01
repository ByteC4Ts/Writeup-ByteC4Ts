from flask import *

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    print(request.headers)
    return open("exp.html").read()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5099)

# ASIS{CSP_1s_n0t_4_sh13ld}
