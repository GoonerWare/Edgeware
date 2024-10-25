from threading import Event


ADDRESS = ("localhost", 6000)
AUTH_KEY = b"EdgewareMultiOS"


def listen(event: Event):
    import logging
    from multiprocessing.connection import Listener

    with Listener(ADDRESS, authkey=AUTH_KEY) as listener:
        with listener.accept() as conn:
            print("connection accepted from", listener.last_accepted)
            while not event.is_set():
                msg = conn.recv()
                if msg == "panic_close":
                    logging.info("Closed after listening to 'panic' packet")
                    event.set()
                    break
