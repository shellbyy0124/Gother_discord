import cProfile

from time import strftime, localtime

def secondsToString(elapsed=None):
    if elapsed is None:
        return strftime("%Y-%m-%d %H:%M:%S", localtime())
    else:
        return str(timedelta(seconds=elapsed))

cProfile.run('secondsToString(elapsed=None)')