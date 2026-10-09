from flask import Flask
import socket

app = Flask(__name__)


@app.route("/")
def hello():
    # The hostname is the container ID, which proves which container served the page.
    return (
        "<h1>Hello, World from Docker!</h1>"
        f"<p>Served by container: {socket.gethostname()}</p>"
    )


if __name__ == "__main__":
    # 0.0.0.0 makes Flask listen on all interfaces so Docker can publish the port.
    app.run(host="0.0.0.0", port=5000)
