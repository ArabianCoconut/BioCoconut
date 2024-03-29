import multiprocessing
import time

from flask import Flask, redirect, url_for
from flask_cors import CORS

import bot

app = Flask(__name__)
CORS(app)


def start_app(host, port, debug=bool()) -> Flask:
    """
    * This is the main function/config for the application
    * @param {string} host
    * @param {string} port
    * @param {bool} debug
    * @return {Flask} app
    """
    if bool(debug) is True:
        app.run(host=host, port=port, debug=debug)
    else:
        print("Debug mode is disabled")
        app.run(host=host, port=port, debug=False)
    return app


@app.route("/")
def index():
    HTML_CODE = """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
  <div class="container mt-5">
    <h2>This is a Server Status Page</h2>
    <p>BioCoconut Server</p>

    <div class="row">
      <div class="col-md-12">
        <div class="card">
          <div class="card-header">
            Server Status
          </div>
          <div class="card-body">
            <p class="card-text">Web Servers : <strong>Active</strong> <img
                src="https://toppng.com/uploads/preview/free-icons-png-green-button-icon-11562980484agrqdnwooe.png"
                height="20px" style="border-radius:50%;" title="Active"></p>
          </div>
          <div class="card-footer text-muted">
            1 Minutes ago
          </div>
        </div>
      </div>
    </div>
    <br>
    <div class="row">
      <div class="col-md-3">
        <div class="card text-white bg-success mb-3" style="max-width: 18rem;">
          <div class="card-header">Web Server</div>
          <div class="card-body">
            <h5 class="card-title">Active</h5>
            <p class="card-text">Web servers are active and usable.</p>
          </div>
        </div>
      </div>
      <br>
      <div class="row text-center border-top">
        <div class="col-md-12">
          <p> BioCoconut Telegram bot &copy; Arabian Coconut</p>
        </div>
      </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
      crossorigin="anonymous">
    </script>
    """
    return HTML_CODE


# Donkey wokring for 10mins to prevent server spin down.
def donkey_work():
    while True:
        multiprocessing.Process(target=bot.main).start()
        time.sleep(600)


@app.route("/donkey")
def donkey():
    multiprocessing.Process(target=donkey_work).start()
    return redirect(url_for("void"))


@app.route("/void")
def void():
    HTML_CODE = """
  <h1>Donkey is working. Go away</h1>
  <button onclick="window.location.href = '/';">Go Back</button>
  """
    return HTML_CODE


if __name__ == "__main__":
    app.run(threaded=True)
