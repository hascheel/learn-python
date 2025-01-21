import datetime

def get_current_time():
    return datetime.datetime.now()

current_time = get_current_time()
print(current_time.strftime("%Y-%m- %H:%M:%S")) # 2021-09-26 15:00:00
print(current_time.strftime("%d.%m.%Y %H:%M:%S")) # 26.09.2021 15:00:00
