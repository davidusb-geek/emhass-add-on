#!/usr/bin/python

import datetime as dt
import time, json
from pathlib import Path

print("Fixing options path")
OPTIONS = "/data/options.json"
options_json = Path(OPTIONS)


def main():

    # Read options info
    print("Initialize infos")
    if options_json.exists():
        with options_json.open('r') as data:
            options = json.load(data)
        seconds_to_publish_data = options['seconds_to_publish_data']
        optimization_task_at = options['optimization_task_at']
        opt_task_at_hour = int(optimization_task_at.split(":")[0])
        opt_task_at_minute = int(optimization_task_at.split(":")[1])
    else:
        print("Error cannot read options.json")
        seconds_to_publish_data = None

    while True:
        if dt.datetime.now().hour == opt_task_at_hour and dt.datetime.now().minute == opt_task_at_minute:
            #some irrelevant function here
            print('Function processing')
            time.sleep(10) 
        else:
            if seconds_to_publish_data is None:
                print("Publishing data every 60s by default...")
                time.sleep(60)
            else:
                print("Publishing data...")
                time.sleep(seconds_to_publish_data)
            continue 

if __name__ == '__main__':
    print("Init main function...")
    main()
