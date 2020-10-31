import datetime
from datetime import date

import atexit

from apscheduler.schedulers.background import BackgroundScheduler

from app import db
from models import Urls


def get_all_expiration_url():
    current_timestamp = date.today()
    print(current_timestamp)
    data_list = Urls.query.filter_by(expiration=current_timestamp).all()
    for data in data_list:
        db.session.delete(data)
        db.session.commit()
        data = Urls.query.filter_by(expiration=current_timestamp).first()


scheduler = BackgroundScheduler()
scheduler.add_job(func=get_all_expiration_url, trigger="interval", days=1)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())
