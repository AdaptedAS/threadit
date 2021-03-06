import threading


class ThreadIT:
    def __init__(self, func, *args, **kwargs):
        self.name = func.__name__
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.job_result = None
        self.thread = self._start_thread()

    def _start_job(self, *args, **kwargs):
        self.job_result = self.func(*args, **kwargs)

    def _start_thread(self):
        thread = threading.Thread(target=self._start_job, args=self.args, kwargs=self.kwargs)
        thread.start()
        return thread

    def doing_work(self):
        return self.thread.is_alive()

    def result(self, timeout: int = None):
        self.thread.join(timeout=timeout)
        return self.job_result


class ParseIT:
    def __init__(self, function=callable, work=list, threads=4, **kwargs):
        self.threads = threads
        self.func = function
        self.items = work
        self.kwargs = kwargs
        self.workers = []
        self.amount = int(len(work) / threads) if int(len(work)) >= 1 else 1
        self.end = self.amount
        self.start = 0
        self.job_result = []
        self.start_work = self._run()

    def _run(self):
        for i in range(self.threads):
            if i + 1 == int(self.threads):
                self.end = len(self.items)
            worker = ThreadIT(self.func, self.items[self.start:self.end], **self.kwargs)
            self.workers.append(worker)
            self.start += self.amount
            self.end += self.amount
        return True

    def status(self, string=True, json=False):
        active = 0
        for worker in self.workers:
            if worker.doing_work():
                active += 1

        if json:
            return {'active': active, 'total': self.threads}

        if string:
            return f'{active} of {self.threads} threads working'

    def doing_work(self):
        for worker in self.workers:
            if worker.doing_work():
                return True
        return False

    def result(self, timeout: int = None, joined=False) -> list:
        for worker in self.workers:
            res = worker.result(timeout=timeout)
            self.job_result.append(res)

        if joined:
            result = []
            for item in self.job_result:
                if item is not None:
                    result.extend(item)
            return result

        return self.job_result