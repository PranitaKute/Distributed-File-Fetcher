from flask import Flask, send_file, jsonify
import os

app = Flask(__name__)

@app.route('/get/<filename>')
def get_file(filename):
    if os.path.exists(filename):
        return send_file(filename)
    return jsonify({"message": "File not found"}), 404

if __name__ == "__main__":
    import sys
    port = int(sys.argv[1])
    app.run(port=port)