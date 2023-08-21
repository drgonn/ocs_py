#!/usr/bin/env python
import os
from app import create_app, db , celery
from app.models import Stock
from flask.cli import FlaskGroup

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


if __name__ == '__main__':
    cli = FlaskGroup(create_app=create_app)
    cli()