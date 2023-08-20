from flask import  jsonify

from app.apiv1 import api



@api.route('/test', methods=['POST','GET'])
def test():
	return jsonify({
			"success": True,
			"error_code": -2,
			"errmsg": "test success 1",
		})