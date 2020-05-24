#!/usr/bin/python3.8

from flask import Flask, jsonify, request, g, render_template
from flask_cors import CORS
import json
import sqlite3

app = Flask(__name__)
CORS(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('data.db')
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/addEvent', methods=['POST'])
def add_event():

    try:
        data = json.loads(request.data)
        
        cursor = get_db().cursor()
        cursor.execute(f'''
            INSERT INTO motion_event(deviceID, deviceName, timestamp)
            VALUES({data['deviceID']}, '{data['deviceName']}', {data['timestamp']});
        ''')
        cursor.execute('COMMIT')

        return jsonify({'msg': 'SUCCESS!'}), 200

    except Exception as e:
        return jsonify({'msg': f'ERROR: {e}'}), 500


@app.route('/events', methods=['GET'])
def events():

    try:
        eid = request.args.get('id')
        dev_id = request.args.get('deviceID')
        dev_name = request.args.get('deviceName')
        lte_timestamp = request.args.get('lte_timestamp')
        gte_timestamp = request.args.get('gte_timestamp')

        cursor = get_db().cursor()

        # [(id, dev_id, dev_name, time), ...]
        events = list( cursor.execute('SELECT * FROM motion_event') )

        if eid:
            events = [e for e in events if int(eid) == e[0]]

        if dev_id:
            events = [e for e in events if int(dev_id) == e[1]]
        
        if dev_name:
            events = [e for e in events if dev_name in e[2]]
        
        if lte_timestamp:
            events = [e for e in events if int(lte_timestamp) >= e[3]]
        
        if gte_timestamp:
            events = [e for e in events if int(gte_timestamp) <= e[3]]
        
        response = { 
            e[0]: {'id': e[0], 'deviceID': e[1], 'deviceName': e[2], 'timestamp': e[3]}
            for e in events
        }

        return jsonify({'msg': 'SUCCESS!', 'data': response}), 200

    except Exception as e:
        return jsonify({'msg': f'ERROR: {e}'}), 500


if __name__ == '__main__':
    app.run(debug=True)