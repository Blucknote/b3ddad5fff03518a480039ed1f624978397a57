import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from time import time
from celery import Celery
from .models import chart_row

app = Celery('proj', result_backend = 'redis://')
#broker='amqp://', result_backend = 'redis://'

@app.task(max_retries=2)
def chart_make(dbid):
    obj = chart_row.objects.get(pk= dbid)
    interval = timedelta(days = int(obj.period))
    dt       = timedelta(hours = int(obj.dt))

    t = np.arange(datetime.now() - interval, datetime.now(), dt)

    plt.plot(t)
    plt.ylabel('Plot')
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
