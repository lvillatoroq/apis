from flask import Flask, jsonify
import gps

app = Flask(__name__)

@app.route('/gps/api/v1/location', methods=['GET'])
def get_gps():
        session = gps.gps("localhost", "2947")
        session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
        while True:
                report = session.next()
                if report['class'] == 'TPV':
                        if hasattr(report, 'time'):
                                return jsonify(clock=report.time,longitude=report.lon,latitude=report.lat)
                                #session.close()
                                break

if __name__ == '__main__':
    app.run(host='0.0.0.0')
