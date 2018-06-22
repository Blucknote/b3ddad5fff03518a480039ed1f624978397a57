import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from time import time
from celery import Celery
from .models import chart_row

app = Celery()
#broker='amqp://', result_backend = 'redis://'

@app.task(max_retries=1)
def chart_make(dbid):
    obj = chart_row.objects.get(pk= dbid)
    print(obj.func)
    interval = timedelta(days = obj.period)
    dt       = timedelta(hours = obj.dt)

    t = np.arange(datetime.now() - _interval, datetime.now(), _dt)

    plt.plot(t)
    plt.ylabel('Plot')
    fig_name = './chs/%s.png' % time()
    plt.savefig(fig_name)
    return fig_name[1:] 

def main():
    x = chart_make.delay(3)
    print(x.get())

if __name__ == '__main__':
    main()