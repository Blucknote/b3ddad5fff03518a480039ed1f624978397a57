import math
import json
import requests
from datetime import datetime, timedelta
from time import time, mktime
from celery import Celery
from .models import chart_row

app = Celery('proj', broker = 'pyamqp://guest@rabbitmq//' , result_backend = 'redis://')

pre_json = {
    'infile': {
        'title': {'text': 'Steep Chart'},
        'xAxis': {'categories': ["Jan", "Feb", "Mar"]},
        'series': [{'data': [29.9, 71.5, 106.4]}]
    }
}

headers = {'Content-Type': 'application/json', 'User-Agent': 'Mozilla'}

@app.task(max_retries=2)
def chart_make(dbid):
    obj = chart_row.objects.get(pk= dbid)
    interval = timedelta(days = int(obj.period))
    dt       = timedelta(hours = int(obj.dt))
    func     = obj.func
   
    now = datetime.now()
    dates = []
    start = now - interval
    dates.append(start)
    
    while start <= now:
        start = start + dt
        dates.append(start)
 
    #x = np.arange(start, now, dt)

    newx = [mktime(_.timetuple()) for _ in dates]
 
    pre_json['infile']['xAxis']['categories'] = newx
   
    try:
        funct = [*map(lambda t: eval(func), newx)]
        pre_json['infile']['series'][0]['data'] = funct
    except Exception as e:
        obj.chart = str(e)
        obj.save()
    else:
        pre_json['infile']['title']['text'] = func
      #  print(pre_json)
        r = requests.post("http://highcharts:8080/", json = pre_json,headers = headers)
        print(r.status_code)
        if r.status_code == 200:
            fig_name = './chs/%s.png' % time()
            graph = open(fig_name,'wb')
            graph.write(r.content)
            graph.close()
            obj.chart = fig_name[1:]
            obj.pub_date = datetime.now()
            obj.save()
            return fig_name[1:]
        else:
            return r.status_code

def main():
	e = chart_make.delay(3)

if __name__ == '__main__':
    main()
