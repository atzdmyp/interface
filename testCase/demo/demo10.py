import threading
import time

condition = threading.Condition()
product = 0
# condition实现复杂同步


class Productor(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global condition, product
        while True:
            if condition.acquire():
                if product < 10:
                    product += 1
                    print("Productor(%s), deliver one, now products %s" % (self.name, product))
                    condition.notify()
                else:
                    print("Productor(%s), already 100, stop product, now peoducts %s" % (self.name, product))
                    condition.wait()
            condition.release()
            time.sleep(1)


class Consumer(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global condition, product
        while True:
            if condition.acquire():
                if product > 1:
                    product -= 1
                    print("Consumer(%s), consum one, now products %s" % (self.name, product))
                    condition.notify()
                else:
                    print("Consumer(%s), only one, stop consum, now products %s" % (self.name, product))
                    condition.wait()
                condition.release()
                time.sleep(1)


if __name__ == "__main__":
    for i in range(0, 2):
        p = Productor()
        p.start()

    for n in range(0, 10):
        c = Consumer()
        c.start()
