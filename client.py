import websocket
import time


def on_message(wsapp, message):
    print(message)
    msg = {'message': "Hello", 'username': "client"}
    wsapp.send(msg)
    print(msg)


wsapp = websocket.WebSocketApp("ws://127.0.0.1:8000/ws/chat/tst/?",
                               header={
                                   "CustomHeader1": "123",
                                   "NewHeader2": "Test"
                               },
                               on_message=on_message)

wsapp.run_forever()
