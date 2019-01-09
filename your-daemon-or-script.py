from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from bt_proximity import BluetoothRSSI
import time
import sys

app = Flask(__name__)
api = Api(app)

class Device(Resource):
	def get(self, address):
		btrssi = BluetoothRSSI(addr=address)
		rssi = btrssi.request_rssi()
		if rssi is None:
			abort(404, message="Device {} doesn't currently exist".format(address))
		else:
			return rssi, 200

api.add_resource(Device, "/device/<string:address>")

if __name__ == "__main__":
	app.run(debug=True)
