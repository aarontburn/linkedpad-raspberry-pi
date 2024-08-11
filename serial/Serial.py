import serial

ser = serial.Serial(
    port='/dev/tty0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

counter = 0


print("Listening to serial: ")
while 1:
    x = ser.readline()
    print(x)