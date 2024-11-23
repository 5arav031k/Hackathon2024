from flask import Flask, request, jsonify
from flask_cors import CORS
from os import makedirs, path

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = './uploads'
makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('api/ai-response', methods=['POST'])
def ai_response():
    try:
        data = request.json
        print("Get data:", data)

        return jsonify({"message": "The data was received"}), 200
    except Exception as e:
        print("Error with data:", str(e))
        return jsonify({"error": str(e)}), 500


@app.route('/api/upload-file', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "File not found in request"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "File not selected"}), 400

    file.save(path.join(UPLOAD_FOLDER, file.filename))
    print(f"File uploaded successfully: {file.filename}")
    return jsonify({"message": f"File {file.filename} successfully uploaded!"}), 200


if __name__ == '__main__':
    app.run(debug=True)