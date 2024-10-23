from flask import Flask

app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return '''
    <h1>This is not a Website 👀</h1>
    <p>This is somekind of Error.</p>
    <a href="/about">Don't go Back</a>
    '''

# About page route
@app.route('/about')
def about():
    return '''
    <h1>About Page</h1>
    <p>This is Cool Website.</p>
    <a href="/">Go Back</a>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Running on port 5000