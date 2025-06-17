from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/version', methods=['GET'])
def version():
    """
    Handles the /version endpoint and returns the current application version.
    """
    app_version = {"Version": "5.0.0"}
    return jsonify(app_version)
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5003)