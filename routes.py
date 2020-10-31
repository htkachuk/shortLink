from flask import request, redirect, jsonify

from app import app, db

from models import Urls
from utils import receive_parameters_for_post, expiretion_to_unixtime
from crypto import get_hash_url


@app.route('/<short_url>', methods=['GET'])
def get_long_url(short_url):
    info = Urls.query.filter_by(short_url=short_url).first()

    # respond
    if info:
        print(info.as_dict())
        return redirect(info.long_url, code=302)
    return "Error url not found"


@app.route('/create_short_url', methods=['POST'])
def create_short_url():
    url, expiration, err = receive_parameters_for_post(
        request, ['url', 'expiration'])
    hash_url = get_hash_url(url)
    experation_timestamp = expiretion_to_unixtime(expiration)

    params = Urls(url, hash_url, experation_timestamp)
    db.session.add(params)
    db.session.commit()
    return jsonify({"short_url": hash_url, "expiration": expiration, "result": "ok"})