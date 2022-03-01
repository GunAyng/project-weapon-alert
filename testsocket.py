from flask_socketio import SocketIO,send,emit
from flask import Flask, jsonify, request, send_from_directory,render_template, Response
import time
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app, cors_allowed_origins="*")
@app.route('/test')
def test():
    socketio.emit('my event',{'url' : 'https://cdn.pixabay.com/photo/2014/08/22/21/45/child-424772_960_720.jpg','detect':'handgun','location':'Floor 1 Zone C Front restaurant cashier','date':'22/02/2022','time':'17:15:59','idcam':'1'})
    return jsonify({'status': 'found'})
 
if __name__ == '__main__':
    print('Server Start')
    socketio.run(app, host='0.0.0.0', port=8000, debug=True)
  
