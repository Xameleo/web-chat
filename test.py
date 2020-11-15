from Client import Client
from threading import Thread
import time
c1 = Client("Adre")
c2 = Client("Kir")



def update_messages():
    """
    updates the local list of messages
    :return: None
    """
    msgs = []
    run = True
    while run:
        time.sleep(0.1)  # update every 1/10 of a second
        new_messages = c1.get_messages()  # get any new messages from client
        msgs.extend(new_messages)  # add to local list of messages

        for msg in new_messages:  # display new messages
            print(msg)

            if msg == "{quit}":
                run = False
                break



Thread(target=update_messages).start()

c2.send_message("hello\n")
c2.send_message("whats up\n")
time.sleep(2)
c1.send_message(" fine\n")
time.sleep(1)
c2.send_message("meh\n")

c2.disconnect()
time.sleep(3)
c1.send_message("cringe\n")
time.sleep(1)
c1.disconnect()
