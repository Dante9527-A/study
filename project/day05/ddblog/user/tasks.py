from django.conf import settings
from tools.sms import YunTongXin
from ddblog.celery import app

@app.task
def send_sms(phone, code):
    x = YunTongXin(settings.AID, settings.ATOKEN, settings.APPID, settings.TID)
    res = x.run(phone, code)
    print(res)