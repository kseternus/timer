import os
import time
from datetime import timedelta
from playsound import playsound


def countdown(user_time):
    raw_time_seconds = (user_time[0]*(60**2) + user_time[1]*60 + user_time[2])
    while raw_time_seconds:
        print('TIMER')
        print(f'{timedelta(seconds=raw_time_seconds)}')
        time.sleep(1)
        raw_time_seconds -= 1
        os.system('cls')
    print('TIME ENDED!')
    playsound('alarm.mp3')  # https://pixabay.com/sound-effects/clock-alarm-8761/


user_time = input("Enter a time (HH:MM:SS): ").split(':')
user_time = [int(i) for i in user_time]

countdown(user_time)
