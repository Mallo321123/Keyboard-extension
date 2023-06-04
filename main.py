import configparser
import serial
from pynput.keyboard import Key, Controller

config = configparser.ConfigParser()                #conf.ini auslesen
config.read("config.ini")
serielle_info = config["serielle_info"]
schnitstelle = serielle_info["schnitstelle"]

keyboard = Controller()                             # keyboard setup

serial = serial.Serial(schnitstelle)                 # serielle setup
serial.baudrate = 9600
serial.timeout = None

def serielle():                                     # serielle auslesen
    serial_roh = serial.readline()              # auslesen
    tmp = serial_roh.decode("latin-1")          # decoden
    output = int(tmp)                           # in int wert umwandeln
    return(output)

def tasten_druck(nummer):
    print(nummer)
    if (nummer == 1):
        keyboard.press(Key.ctrl_l)
        keyboard.press(Key.shift_l)
        keyboard.press(Key.f1)
        keyboard.release(Key.f1)
        keyboard.release(Key.shift_l)
        keyboard.release(Key.ctrl_l)
    if (nummer == 2):
        keyboard.press(Key.ctrl_l)
        keyboard.press(Key.shift_l)
        keyboard.press(Key.f2)
        keyboard.release(Key.f2)
        keyboard.release(Key.shift_l)
        keyboard.release(Key.ctrl_l)
    if (nummer == 3):
        keyboard.press(Key.ctrl_l)
        keyboard.press(Key.shift_l)
        keyboard.press(Key.f3)
        keyboard.release(Key.f3)
        keyboard.release(Key.shift_l)
        keyboard.release(Key.ctrl_l)
    if (nummer == 4):
        keyboard.press(Key.ctrl_l)
        keyboard.press(Key.shift_l)
        keyboard.press(Key.f4)
        keyboard.release(Key.f4)
        keyboard.release(Key.shift_l)
        keyboard.release(Key.ctrl_l)
    if (nummer == 5):
        keyboard.press(Key.ctrl_l)
        keyboard.press(Key.shift_l)
        keyboard.press(Key.f5)
        keyboard.release(Key.f5)
        keyboard.release(Key.shift_l)
        keyboard.release(Key.ctrl_l)
    if (nummer == 6):
        keyboard.press(Key.ctrl_l)
        keyboard.press(Key.shift_l)
        keyboard.press(Key.f6)
        keyboard.release(Key.f6)
        keyboard.release(Key.shift_l)
        keyboard.release(Key.ctrl_l)
    if (nummer == 7):
        keyboard.press(Key.ctrl_l)
        keyboard.press(Key.shift_l)
        keyboard.press(Key.f7)
        keyboard.release(Key.f7)
        keyboard.release(Key.shift_l)
        keyboard.release(Key.ctrl_l)
    if (nummer == 8):
        keyboard.press(Key.ctrl_l)
        keyboard.press(Key.shift_l)
        keyboard.press(Key.f8)
        keyboard.release(Key.f8)
        keyboard.release(Key.shift_l)
        keyboard.release(Key.ctrl_l)
    if (nummer == 9):
        keyboard.press(Key.ctrl_l)
        keyboard.press(Key.shift_l)
        keyboard.press(Key.f9)
        keyboard.release(Key.f9)
        keyboard.release(Key.shift_l)
        keyboard.release(Key.ctrl_l)
        
    if (nummer == 10):
        keyboard.press(Key.ctrl_r)
        keyboard.press(Key.shift_r)
        keyboard.press(Key.f1)
        keyboard.release(Key.f1)
        keyboard.release(Key.shift_r)
        keyboard.release(Key.ctrl_r)
    if (nummer == 11):
        keyboard.press(Key.ctrl_r)
        keyboard.press(Key.shift_r)
        keyboard.press(Key.f2)
        keyboard.release(Key.f2)
        keyboard.release(Key.shift_r)
        keyboard.release(Key.ctrl_r)
    if (nummer == 12):
        keyboard.press(Key.ctrl_r)
        keyboard.press(Key.shift_r)
        keyboard.press(Key.f3)
        keyboard.release(Key.f3)
        keyboard.release(Key.shift_r)
        keyboard.release(Key.ctrl_r)
    if (nummer == 13):
        keyboard.press(Key.ctrl_r)
        keyboard.press(Key.shift_r)
        keyboard.press(Key.f4)
        keyboard.release(Key.f4)
        keyboard.release(Key.shift_r)
        keyboard.release(Key.ctrl_r)

while True:                                         # main loop
    input = serielle()
    tasten_druck(input)