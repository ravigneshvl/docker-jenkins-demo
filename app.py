from flake import Flake

app = Flake(__name__)
@app.route("/")
def home():
    return "CICD with Flake is working!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)