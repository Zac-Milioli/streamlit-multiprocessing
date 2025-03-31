from time import sleep
from datetime import datetime

def random_time_process(random_number: int):
    sleep(random_number)
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    return f"Thread of {random_number} seconds done ({hour}:{minute}:{second})"
