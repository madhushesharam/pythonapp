import logging
import random
from flask import Flask
from datetime import datetime

app = Flask(__name__)

logging.basicConfig(filename='record.log', level=logging.DEBUG)

@app.route('/')
def index():
    app.logger.info('Info level log')
    app.logger.warning('Warning level log')
    return {"date": datetime.utcnow(), "numberofPodsRequired": random.randint(0,9)}

app.run(host='0.0.0.0',debug=True)