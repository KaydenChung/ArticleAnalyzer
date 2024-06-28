# Library Imports
from flask import Flask, render_template, request, redirect, url_for
import PyPDF2

# Creating Flask App
app = Flask(__name__)

# Extract Text from PDF
def extractText(file):
    text = ""
    try:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    except Exception as e:
        print(f"Error Reading PDF: {e}")
    return text

# Search Keywords in Text
def searchKeywords(filename, text, keywords):
    # Split Text into Sentences
    sentences = []
    current_sentence = ""
    for char in text:
        if char in '.!?':
            if current_sentence:
                sentences.append(current_sentence.strip())
                current_sentence = ""
        else:
            current_sentence += char
    if current_sentence:
        sentences.append(current_sentence.strip())

    # Add Relevant Sentences to Data
    data = []
    for keyword in keywords:
        counter = 1
        for sentence in sentences:
            if (len(sentence) < 400) and (keyword.lower() in sentence.lower()):
                data.append({'filename': filename, 'keyword': keyword, 'count': counter, 'sentence': sentence.strip()})
                counter += 1
    return data

# Flask App Handling
@app.route("/", methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        files = request.files.getlist('articles')[::-1]
        unfilteredKeywords = request.form['keywords'].split(',')
        keywords = [keyword.strip() for keyword in unfilteredKeywords if keyword.strip()]
        extendedData = []
        for file in files:
            if file and file.filename.endswith('.pdf'):
                # Extract Text from PDF
                text = extractText(file)
                if not text:
                    return f"No text extracted from {file.filename}."
                # Search Keywords in Text
                data = searchKeywords(file.filename, text, keywords)
                extendedData.extend(data)
            else:
                return f"Invalid File Format: {file.filename}. Please upload a PDF file."
        return render_template('results.html', data=extendedData)
    return render_template('index.html')

# Main
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)