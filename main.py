import time
import concurrent.futures
from flask import Flask, request, jsonify

app = Flask(__name__)
executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)


def create(id):
    time.sleep(10)
    print(id)


@app.route('/create', methods=['GET'])
def create_subtitle():
    id = request.args.get('id')
    executor.submit(create, id)
    return jsonify({"message": "File creation in progress"})


if __name__ == '__main__':
    app.run()
 
