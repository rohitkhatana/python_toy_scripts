import json
import datetime

"""def handler1(obj):
    if isinstance(obj,datetime.datetime):
        return obj.isoformat()
    else: return None
 
dth = handler1(datetime.datetime.now())"""
#dth = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None


print json.dumps(datetime.datetime.now(), default=dth)
