import base64
from flask import Flask, render_template, request, Response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'cr1z' and password == '54378121':
            return 'Success'
        else:
            return 'Failure'
        
@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files.get('file')
    if file.content_type == 'text/plain':
        data = file.read()
        l1 = base64.b64encode(data)
        result = l1.decode()

        with open('result.txt', 'w') as output_file:
            output_file.write(result)
        
        response = Response(
            result, 
            mimetype='text/plain',
            headers={
                'Content-Disposition': 'attachment; filename=result.txt'
            }
        )

        return response

    else:
        return 'This file is not supported...'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')