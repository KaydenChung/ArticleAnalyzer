# Project Title

Article Analyzer

## Description

Online PDF Article Keyword Analyzing Tool  
Developed by Kayden Chung  
Assisted by Ali Al-Reda El-Zein  
Created for Manufactured Ecosystems Research

### Setup

* Clone the Repository
```
git clone https://github.com/KaydenChung/ArticleAnalyzer.git
```
* Allow Windows to Run Scripts
```
Set-ExecutionPolicy Unrestricted -Scope Process
```
* Create Virtual Environment
```
python -m venv .venv
```
* Activate Virtual Environment
#### Windows:
```
.venv\Scripts\activate
```
#### MacOS and Linux:
```
source .venv/bin/activate
```

### Execution

* Install Required Dependencies
```
pip install -r requirements.txt
```
* Run the Flask App
```
flask --app flaskr:app run --debug
```