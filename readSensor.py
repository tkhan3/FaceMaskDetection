import serial
import time

def main():
    print ("inside main")
    ser = serial.Serial('COM5', 115200)
    #ser = serial.Serial('COM3', 9600)

    data = []

    while (True):
        b = ser.readline()
        string_n = b.decode()
        print (string_n)

    #for i in range(5000):
    #    b = ser.readline()
    #    string_n = b.decode()
    #    print (string_n)

if __name__ == "__main__":
    main()