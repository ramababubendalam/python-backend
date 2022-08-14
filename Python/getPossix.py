import json
import time
import datetime


def lambda_handler(event, context):
    # TODO implement

    epoch_time = int(time.time())
    # now = datetime.now()
    # now_with_tz = now.astimezone()
    # my_timezone = now_with_tz.tzinfo
    local_timezone = datetime.datetime.utcnow().astimezone().tzinfo
    jsonStr = json.dumps(local_timezone, indent=1, sort_keys=True, default=str)

    return {
        'epochTime': epoch_time,
        'ServerTimeZone': json.loads(jsonStr)
    }

