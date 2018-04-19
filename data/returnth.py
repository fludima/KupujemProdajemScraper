from threading import Thread

# main functionality is I/O bound so we use threading instead of
# mutliprocessing


class ThreadReturn(Thread):
    '''
    Creating a thread that also returns a value

    As known the threading.Thread does not offer a return value unless
    we place it in a que or save it in another placeholder.
    This code only overrides that part of the code so that it will return 
    a value when we call .value(), 
    i.e. after we use .join() - finish the job (thread-finishes_job) 

    Extends:
        Thread
    '''

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        Thread.__init__(self, group, target, name, args, kwargs, daemon=daemon)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self):
        Thread.join(self)

    def value(self):
        return self._return
