def get_hour(epoch_seconds): 
    return epoch_seconds // 3600

def get_minutes(epoch_seconds):
    return (epoch_seconds - get_hour(epoch_seconds) * 3600) // 60

def get_seconds(epoch_seconds):
    return epoch_seconds - (get_minutes(epoch_seconds) * 60) - (get_hour(epoch_seconds) * 3600)
