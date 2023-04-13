from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_header_data():
    header_data = {}
    for key, value in request.headers.items():
        header_data[key] = value
    return header_data

if __name__ == '__main__':
    app.run()
