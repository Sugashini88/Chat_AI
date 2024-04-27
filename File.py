from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import tempfile
import subprocess

app = Flask(__name__)

# Configuration for file uploads
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check if a filename has an allowed extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return jsonify({'message': 'File uploaded successfully', 'filename': filename})
    
    return jsonify({'error': 'Invalid file'})

@app.route('/process-pdf/<filename>', methods=['GET'])
def process_pdf(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    # Example: Extract text from PDF using pdftotext (you may need to install pdftotext)
    output_text = subprocess.check_output(['pdftotext', filepath, '-']).decode('utf-8')
    
    # Perform any other processing on the PDF content here
    
    return jsonify({'text': output_text})

if __name__ == '__main__':
    app.run(debug=True)
