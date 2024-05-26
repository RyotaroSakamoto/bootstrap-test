from flask import Flask, request, jsonify
import pandas as pd
from io import BytesIO
import PyPDF2

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'pdf' not in request.files:
        return jsonify({'error': 'No file uploaded.'}), 400

    pdf_file = request.files['pdf']
    pdf_reader = PyPDF2.PdfFileReader(BytesIO(pdf_file.read()))
    # サンプル処理として、PDFのメタデータを抽出
    data = {
        'Title': pdf_reader.getDocumentInfo().title,
        'Author': pdf_reader.getDocumentInfo().author,
        'Number of Pages': pdf_reader.getNumPages()
    }

    df = pd.DataFrame([data])
    return df.to_json(orient='records')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
