from flask import Flask, request, jsonify, session
from flask_cors import CORS
from os import makedirs, path
import secrets
import converter
import openAI

app = Flask(__name__)
CORS(app)
app.secret_key = secrets.token_hex(32)

UPLOAD_FOLDER = './uploads'
makedirs(UPLOAD_FOLDER, exist_ok=True)

NO_FILENAME_SET = 'No file name set'


@app.route('/api/ai-response', methods=['POST'])
def ai_response():
    try:
        user_request = request.json
        print("User request: ", user_request)

        file_name = session.get('file_name', NO_FILENAME_SET)
        if file_name is NO_FILENAME_SET:
            return jsonify({"error": NO_FILENAME_SET}), 400

        json_data = converter.convert_file_to_json(file_name)
        gpt_response = openAI.analyze_dataset_with_gpt(json_data, user_request)

        return jsonify({"gpt_response": gpt_response}), 200
    except Exception as e:
        print("Error with data:", str(e))
        return jsonify({"error": str(e)}), 400


@app.route('/api/upload-file', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "File not found in request"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "File not selected"}), 400

    session['file_name'] = file.filename

    # Сохраняем файл
    file.save(path.join(UPLOAD_FOLDER, file.filename))
    print(f"File uploaded successfully: {file.filename}")
    return jsonify({"message": f"File {file.filename} successfully uploaded!"}), 200


if __name__ == '__main__':
    app.run(debug=True)
