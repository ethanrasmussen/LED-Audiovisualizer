from flask import Flask
from flask import *


# init Flask app
app = Flask(__name__)

# index route
@app.route('/')
def index():
    return render_template('index.html')

# led trigger route

# run app
if __name__ == '__main__':
    app.run(port=80)