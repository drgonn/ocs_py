import time
import os

from flask import Flask, jsonify
from app import celery



@celery.task
def async_task():
    # 在这里执行异步任务，可以是耗时的操作
    file_content = "Hello, this is the sync celery content of the file."
    file_path = "example.txt"

    with open(file_path, "w") as file:
        file.write(file_content)

    time.sleep(10)
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted.")
    else:
        print(f"File '{file_path}' does not exist.")


    return 'Async task completed'



