from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def upload_page():
    if 'dataset' not in request.files:
        return 'No file part'

    file = request.files['dataset']
    if file.filename == '':
        return 'No selected file'

    if file:
        ##yariks_method(file)
        return f'File {file.filename} successfully added to yariks method'