import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from time import time

def chart_make(func, interval, dt):
    _interval = timedelta(days = interval)
    _dt       = timedelta(hours = dt)

    t = np.arange(datetime.now() - _interval, datetime.now(), _dt)

    plt.plot(t)
    plt.ylabel('Plot')
    fig_name = './chs/%s.png' % time()
    plt.savefig(fig_name)
    return fig_name[1:] 
