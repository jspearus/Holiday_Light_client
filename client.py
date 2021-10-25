import socket
import datetime
import holidays

# todo add list of holidays
Holidays = [
    "New Year's Day", "Memorial Day", "Independence Day", "Halloween",
    "Thanksgiving", "Christmas Day"
]
#todo add holiday to list of holidays
hList = holidays.US(years=2021).items()
# hList.addItem(datetime.date(2021, 10, 31), "Halloween")
# print(hList)


def getNxtHoliday():
    global nxtHoliday
    global nxtDate
    for date, name in sorted(hList):
        print(name, date)
        if datetime.date.today() < date and name in Holidays:
            nxtDate = date
            nxtHoliday = name
            break


print(datetime.date.today())
getNxtHoliday()

HEADER = 64
PORT = 5000
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "dgscore.ddns.net"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send("Hello World!")
while True:
    smsg = input("enter msg: \n")
    if smsg == 'q':
        break
    elif smsg == 'holiday':
        smsg = nxtHoliday
    send(smsg)

send("Goodby Jeff!")
send(DISCONNECT_MESSAGE)
