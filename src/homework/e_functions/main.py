from value_return import get_hour
from value_return import get_minutes
from value_return import get_seconds

def get_time(epoch_seconds):
    hours = str(get_hour(epoch_seconds))
    minutes = str(get_minutes(epoch_seconds))
    seconds = str(get_seconds(epoch_seconds))

    hours = "0" + hours if len(hours) == 1 else hours
    minutes = "0" + minutes if len(minutes) == 1 else minutes
    seconds = "0" + seconds if len(seconds) == 1 else seconds

    return hours + ":" + minutes + ":" + seconds

print(get_time(3800))