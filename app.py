import logging
from flask import Flask, render_template

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home(event=None, context=None):
    logger.info('Lambda Invoked Index....')
    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug=True)

