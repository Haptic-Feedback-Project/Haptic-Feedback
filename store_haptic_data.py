import serial
import struct
import time

# Class to store data collected from a sensor
class Motion_Data:

    def __init__(self):
      
      # initalize motion data for one sensor
      self.i = []
      self.j = []
      self.k = []
      self.phi = []
      self.theta = []
      self.psi = []


def main():
    ser = serial.Serial('/dev/ttyACM0', 38400)
    ser.flush()
    ser.flushInput()
    ser.flushOutput()
    time.sleep(1)
    
    sensor_array = [Motion_Data(), Motion_Data(), Motion_Data()]
    file = open('haptic_data.txt', 'w+')

    count = 0
    frame_header1 = struct.unpack('b', ser.read())[0]
    frame_header2 = struct.unpack('b', ser.read())[0]
    
    while(count < 100):
        #frame_header1 = struct.unpack('b', ser.read())[0]
        #frame_header2 = struct.unpack('b', ser.read())[0]
        # Header packet is 0x8000(which is -128 and 0 if single bytes)
        if frame_header1 == -128: 
            #Only read in data if header packet is found           
            if frame_header2 == 0:
                #Write what sensor it belongs to?
                file.write(str(get_motion_data(ser)) + '\n')              
                file.write(str(get_motion_data(ser)) + '\n') 
                file.write(str(get_motion_data(ser)) + '\n')               
                file.write(str(get_motion_data(ser)) + '\n')                
                file.write(str(get_motion_data(ser)) + '\n')               
                file.write(str(get_motion_data(ser)) + '\n')

                frame_header1 = struct.unpack('b', ser.read())[0]
                frame_header2 = struct.unpack('b', ser.read())[0]

                count += 1
            else:
                frame_header1 = frame_header2
                frame_header2 = struct.unpack('b', ser.read())[0]
        else:
            frame_header1 = frame_header2
            frame_header2 = struct.unpack('b', ser.read())[0]
        
    file.close()
    ser.close()
# Retrieve data from sensor
def get_motion_data(ser):
    # Arduino sends in 1 bytes so read in first 8 bits, 
    # shifting them to the left and getting the next 8
    """
    sensor_data = struct.unpack('b', ser.read())[0]
    print(sensor_data)
    sensor_data2 = struct.unpack('b', ser.read())[0]
    print(sensor_data2)
    """
    sensor_data = struct.unpack('b', ser.read())[0]
    sensor_data2 = struct.unpack('b', ser.read())[0]
    sensor_data3 = (sensor_data << 8) | sensor_data2

    print(sensor_data3)

    return sensor_data3

# helper function to determine sign bit
def convert(x):
    if x > 32768:
        x -= 65536
    return x

if __name__ == "__main__":
    main()
