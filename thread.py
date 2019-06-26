import threading

class VarunsMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = VarunsMessenger(name='Send out messages.')
y = VarunsMessenger(name='Recieve messages.')
x.start()
y.start()