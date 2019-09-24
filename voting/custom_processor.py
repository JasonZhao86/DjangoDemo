import datetime

def debugging(request):
    return {"nowtime": datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")}