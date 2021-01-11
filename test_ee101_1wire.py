import time
import serial

def EE101Text(channel, text):
    EE101_SYNC = 0x50
    EE101_TEXT_TYPE = 0x00
    ser.write(bytes([(int(channel) & 0x07) | EE101_SYNC | EE101_TEXT_TYPE]))
    ser.write(text.encode())
    ser.write(bytes([0]))
    
def EE101Value(channel, value):
    EE101_SYNC = 0x50
    EE101_VALUE_TYPE = 0x80
    ser.write(bytes([(int(channel) & 0x07) | EE101_SYNC | EE101_VALUE_TYPE]))
    ser.write(bytes([(int(value >> 24))]))
    ser.write(bytes([(int(value >> 16))]))
    ser.write(bytes([(int(value >> 8))]))
    ser.write(bytes([(int(value) & 0xFF)]))

print("Press CTL+C to exit program")

ser = serial.Serial("/dev/serial0")
time.sleep(1)

try:

    i = 0
    
    while True:
        EE101Text(0,"Hello")
        EE101Text(1,"Tim")
        EE101Text(2,"this")
        EE101Text(3,"is")
        EE101Text(4,"your")
        EE101Text(5,"ee101")
        EE101Text(6,"ported to")
        EE101Text(7,"Python")

        i += 1

        EE101Value(0, i)                                           
        EE101Value(1, i)                                          
        EE101Value(2, i)
        EE101Value(3, i)
        EE101Value(4, i)
        EE101Value(5, i)
        EE101Value(6, i)
        EE101Value(7, i)
        
except KeyboardInterrupt:
    print("Exiting Program")

except:
    print("Error Occurs, Exiting Program")

finally:
    ser.close()
pass