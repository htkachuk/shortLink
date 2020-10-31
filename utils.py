import datetime
from datetime import date

from models import Urls


def receive_parameters(data, parameter_names):
    errors = []
    parameters = []
    for parameter in parameter_names:
        if parameter in data.keys():
            parameters.append(data[parameter])
        else:
            parameters.append(None)
            errors.append(parameter)
    if errors:
        error_msg = "Missing parameters:"
        for error in errors:
            error_msg += f' {error},'
        errors = f'{error_msg[:-1]}.'
    else:
        errors = None
    parameters.append(errors)
    return tuple(parameters)


def receive_parameters_for_post(request, parameter_names):
    data = request.get_json()
    return receive_parameters(data, parameter_names)


def expiretion_to_unixtime(expiration):
    current_timestamp = date.today()
    return current_timestamp + datetime.timedelta(days=int(expiration))


def check_for_adding(short_url, expiration_date):
    dataList = Urls.query.filter_by(short_url=short_url).all()
    for data in dataList:
        if str(data.expiration) == str(expiration_date):
            return False

    return True
