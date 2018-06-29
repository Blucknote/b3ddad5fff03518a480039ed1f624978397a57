import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from time import time, mktime
from celery import Celery
from .models import chart_row

app = Celery('proj', broker = 'pyamqp://guest@rabbitmq//' , result_backend = 'redis://')

@app.task(max_retries=2)
def chart_make(dbid):
    obj = chart_row.objects.get(pk= dbid)
    interval = timedelta(days = int(obj.period))
    dt       = timedelta(hours = int(obj.dt))
    func     = obj.func
   
    now = datetime.now()
    start = now - interval
     
    x = np.arange(start, now, dt)

    newx = [mktime(_.astype(datetime).timetuple()) for _ in x]
    
    try:
        funct = [*map(lambda t: eval(func), newx)]
        plt.plot(funct)
    except Exception as e:
        obj.chart = str(e)
        obj.save()
    else:
        plt.ylabel(func)
        fig_name = './chs/%s.png' % time()
        plt.savefig(fig_name)
        obj.chart = fig_name[1:]
        obj.pub_date = datetime.now()
        obj.save()
        return fig_name[1:]

def main():
    x = chart_make.delay(3)

if __name__ == '__main__':
    main()
