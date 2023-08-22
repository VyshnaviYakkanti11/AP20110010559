from flask import Flask, request, jsonify
import requests
import time

app = Flask(__name__)

@app.route('/numbers', methods=['GET'])
def retrieve_numbers():
    urls = request.args.getlist('url')
    result = []

    for url in urls:
        try:
            start_time = time.time()
            response = requests.get(url, timeout=0.5)  
            end_time = time.time()

            if response.status_code == 200 and (end_time - start_time) <= 0.5:
                json_data = response.json()
                if 'numbers' in json_data:
                    result.extend(json_data['numbers'])
        except Exception as e:
            pass  

    unique_numbers = list(set(result))  
    unique_numbers.sort()  

    return jsonify({'numbers': unique_numbers})

if __name__ == '_main_':
    app.run(host='localhost', port=3000)