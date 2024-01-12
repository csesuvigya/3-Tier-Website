from flask import Flask, render_template, request

app = Flask(__name__)

# Read data from the CSV file
def read_data():
    data = []
    with open('data.csv', 'r') as file:
        lines = file.readlines()
        headers = lines[0].strip().split(',')
        for line in lines[1:]:
            values = line.strip().split(',')
            entry = dict(zip(headers, values))
            data.append(entry)
    return data

# Search function based on user input
def search(data, query, category):
    results = []
    for entry in data:
        if query.lower() in entry[category].lower():
            results.append(entry)
    return results

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_results():
    query = request.form['query']
    category = request.form['category']
    data = read_data()
    results = search(data, query, category)
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
