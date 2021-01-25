from flask import Flask, render_template, send_from_directory, Request
from flask_socketio import SocketIO, emit
import flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.debug = True

socketio = SocketIO(app)

@app.route('/')
def index():
    return send_from_directory(".","index.html", as_attachment=False)

@app.route('/socket.io.js')
def socket_file():
    return send_from_directory(".","socket.io.js", as_attachment=False)

@app.route('/d3.v6.js')
def d3_file():
    return send_from_directory(".","d3.v6.js", as_attachment=False)

@app.route('/reading/', methods={"GET"})
def get_readings():
	rq = flask.request
	data = rq.get_json()

	return flask.jsonify(result='OK')

@socketio.on('sensor reading event')
def test_sensor(message):
    emit('sensor reading broadcast', {'data': message['data']}, broadcast=True)

@app.after_request
def add_header(response):
  response.headers['Access-Control-Allow-Origin'] = "*"
  response.headers['Access-Control-Allow-Headers'] = "*"

  return response

@app.teardown_appcontext
def shutdown_session(exception=None):
    pass

if __name__ == '__main__':
    socketio.run(app)