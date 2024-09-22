from flask import Flask, request, jsonify, render_template, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['article_db']
collection = db['article_titles']

@app.route('/')
def index():
    articles = list(collection.find({}, {'_id': 0}))
    return render_template('index.html', articles=articles)

@app.route('/add', methods=['POST'])
def add_article():
    title = request.form.get('title')
    if title:
        collection.insert_one({'title': title})
    return redirect(url_for('index'))

@app.route('/delete/<title>', methods=['POST'])
def delete_article(title):
    collection.delete_one({'title': title})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)