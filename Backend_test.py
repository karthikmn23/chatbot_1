from flask import Flask, request, jsonify

app = Flask(__name__)

def foo(request_id, query):
    print("Works")
    flag = 0
    base64_img, remarks = "some value", "some value"
    return flag, request_id, base64_img, remarks

@app.route('/process_query', methods=['POST'])
def process_query():
    data = request.get_json()
    request_id = data.get('request_id')
    query = data.get('query')
    
    if not request_id or not query:
        return jsonify({'status': 'error', 'message': 'Invalid input'}), 400
    
    flag, req_id, base64_img, remarks = foo(request_id, query)
    return jsonify({
        'status': 'success',
        'flag': flag,
        'request_id': req_id,
        'base64_img': base64_img,
        'remarks': remarks
    })

if __name__ == '__main__':
    app.run(debug=True)
