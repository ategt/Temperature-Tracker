from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.debug = True

socketio = SocketIO(app)

@app.route('/')
def index():
    #return render_template('index.html')
    return send_from_directory(".","index.html", as_attachment=False)

@app.route('/socket.io.js')
def socket_file():
    return send_from_directory(".","socket.io.js", as_attachment=False)

@socketio.on('my event')
def test_message(message):
    emit('my response', {'data': message['data']})

@socketio.on('my broadcast event')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app)
    #app.run()