from flask import Flask, send_file, redirect
import sys

if len(sys.argv) > 1:
        try:
                file_name = sys.argv[1]
                port = int(sys.argv[2])
        except:
                print('Incorrect arguments!')
else:
    file_name = input('Enter file name: ')

    try:
        port = int(input('Enter port: '))
    except:
        print('Incorrect file name!')

app = Flask('srv')

@app.route('/')
def index():
    return redirect('/' + file_name)

@app.route('/' + file_name)
def ret_file():
    print('Sending file to the client.')
    return send_file(file_name)

app.run(host='0.0.0.0', debug=False, port=port)
