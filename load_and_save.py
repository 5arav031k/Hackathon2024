from flask import Flask, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = './datasets'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'csv', 'xlsx'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/', methods=['POST'])
def upload_page():
    if 'dataset' not in request.files:
        return 'No file part'

    file = request.files['dataset']
    if file.filename == '':
        return 'No selected file'

    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    if file and allowed_file(file.filename):

        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        return f'File successfully uploaded and saved as {filename}'
    else:
        return 'Invalid file format. Only CSV and Excel files are allowed.'


# if __name__ == '__main__':
#     if not os.path.exists(app.config['UPLOAD_FOLDER']):
#         os.makedirs(app.config['UPLOAD_FOLDER'])
#     app.run(debug=True)
