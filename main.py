from datetime import datetime

from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/check')
def check():
    return jsonify({'ip': request.remote_addr, 'now': datetime.now().isoformat()}), 200


if __name__ == "__main__":
    app.run()
