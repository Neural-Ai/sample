import subprocess
from flask import Flask

app = Flask(__name__)

def start_rasa():
    actions_cmd = ['rasa', 'run', 'actions']
    rasa_cmd = ['rasa', 'run', '--model', 'models', '--enable-api', '--cors', '*', '-credentials', 'credentials.yaml']
    subprocess.Popen(actions_cmd)
    subprocess.Popen(rasa_cmd)
    print('Rasa started successfully!')

start_rasa()

@app.route('/')
def home():
    return 'Hello, world!'
