import time
from datetime import datetime, timezone, timedelta
from flask import  jsonify

from app.apiv1 import api
from app.task.task import async_task



@api.route('/test', methods=['POST','GET'])
def test():
	return jsonify({
			"success": True,
			"error_code": -2,
			"errmsg": "test success 1",
		})

@api.route('/test/sync', methods=['POST','GET'])
def test_sync():
	async_task.delay()
	
	print("test sync", time.time())
	return jsonify({
			"success": True,
			"error_code": -2,
			"errmsg": f"test sync {time.time()}",
		})

@api.route('/test/time/<int:id>', methods=['POST','GET'])
def test_time(id):
	r = convert_timestamp_to_timezones(id)
	for tz, time in r.items():
		print(f"{tz}: {time}")

	now = get_current_time_in_timezones()
	return jsonify({
			"success": True,
			"error_code": 0,
			"data": r,
			"now": now,
		})




def convert_timestamp_to_timezones(timestamp_ms):
    # 将毫秒级别时间戳转换为秒级别时间戳
    timestamp_seconds = timestamp_ms / 1000
    
    # 创建一个 datetime 对象，使用 UTC 时间
    utc_datetime = datetime.fromtimestamp(timestamp_seconds, tz=timezone.utc)
    
    # 设置不同的时区
    beijing_tz = timezone(timedelta(hours=8))  # 北京时间 UTC+8
    new_york_tz = timezone(timedelta(hours=-4))  # 纽约时间 UTC-4
    chicago_tz = timezone(timedelta(hours=-5))  # 芝加哥时间 UTC-5
    
    # 根据不同时区生成对应的时间
    beijing_time = utc_datetime.astimezone(beijing_tz)
    new_york_time = utc_datetime.astimezone(new_york_tz)
    chicago_time = utc_datetime.astimezone(chicago_tz)
    
    return {
        "UTC": str(utc_datetime),
        "北京": str(beijing_time),
        "New York": str(new_york_time),
        "Chicago": str(chicago_time)
    }

def get_current_time_in_timezones():
    # 获取当前时间的 datetime 对象，使用 UTC 时间
    current_utc_time = datetime.now(timezone.utc)
    
    # 设置不同的时区
    beijing_tz = timezone(timedelta(hours=8))  # 北京时间 UTC+8
    new_york_tz = timezone(timedelta(hours=-4))  # 纽约时间 UTC-4
    chicago_tz = timezone(timedelta(hours=-5))  # 芝加哥时间 UTC-5
    
    # 根据不同时区生成对应的时间字符串
    beijing_time = current_utc_time.astimezone(beijing_tz).strftime('%Y-%m-%d %H:%M:%S %Z')
    new_york_time = current_utc_time.astimezone(new_york_tz).strftime('%Y-%m-%d %H:%M:%S %Z')
    chicago_time = current_utc_time.astimezone(chicago_tz).strftime('%Y-%m-%d %H:%M:%S %Z')
    utc_time = current_utc_time.strftime('%Y-%m-%d %H:%M:%S %Z')
    
    return {
        "Beijing": beijing_time,
        "New York": new_york_time,
        "Chicago": chicago_time,
        "UTC": utc_time
    }