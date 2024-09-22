from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['article_db']
collection = db['article_titles']

def analyze_titles():
    titles = list(collection.find({}, {'_id': 0}))
    word_count = {}
    
    for title in titles:
        words = title['title'].split()
        for word in words:
            word = word.lower()
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    
    sorted_word_count = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
    return sorted_word_count

if __name__ == '__main__':
    analysis = analyze_titles()
    for word, count in analysis:
        print(f"{word}: {count}")