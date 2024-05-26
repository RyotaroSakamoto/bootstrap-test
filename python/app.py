from flask import Flask, request, jsonify
import pandas as pd
from io import BytesIO
import PyPDF2
import requests

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'pdf' not in request.files:
        return jsonify({'error': 'No file uploaded.'}), 400

    pdf_file = request.files['pdf']
    pdf_reader = PyPDF2.PdfFileReader(BytesIO(pdf_file.read()))

    # PDFのテキストを抽出
    text = ""
    for page_num in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page_num)
        text += page.extract_text()

    # サンプルとしてテキストの解析（ここでは単語の数を数える）
    word_count = len(text.split())

    data = {
        'Title': pdf_reader.getDocumentInfo().title,
        'Author': pdf_reader.getDocumentInfo().author,
        'Number of Pages': pdf_reader.getNumPages(),
        'Word Count': word_count
    }

    df = pd.DataFrame([data])
    return df.to_json(orient='records')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
