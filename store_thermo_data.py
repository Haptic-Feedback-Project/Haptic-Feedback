import serial
import struct
import time

def main():
    ser = serial.Serial('/dev/ttyACM0', 38400)
    ser.flush()
    ser.flushInput()
    ser.flushOutput()
    time.sleep(1)

    # 10 minutes
    timeout = time.time() + 60*1
    
    file = open('thermo_data.txt', 'w+')


    frame_header1 = struct.unpack('b', ser.read())[0]
    frame_header2 = struct.unpack('b', ser.read())[0]
    
    while(1):
        #frame_header1 = struct.unpack('b', ser.read())[0]
        #frame_header2 = struct.unpack('b', ser.read())[0]
        # Header packet is 0x8000(which is -128 and 0 if single bytes)
        if frame_header1 == -128 and frame_header2 == 0: 

            # ax
            file.write(str(get_motion_data(ser)) + '\n') 

            #ay             
            file.write(str(get_motion_data(ser)) + '\n') 

            #az
            file.write(str(get_motion_data(ser)) + '\n') 

            #gx
            file.write(str(get_motion_data(ser)) + '\n')

            #gy              
            file.write(str(get_motion_data(ser)) + '\n')

            # gz 
            file.write(str(get_motion_data(ser)) + '\n')

            # temperature               
            file.write(str(get_motion_data(ser)) + '\n') 

            # time              
            file.write(str(get_motion_data(ser)) + '\n')

            frame_header1 = struct.unpack('b', ser.read())[0]
            frame_header2 = struct.unpack('b', ser.read())[0]

        else:
            frame_header1 = frame_header2
            frame_header2 = struct.unpack('b', ser.read())[0]                     

        if time.time() > timeout:    
            break    
        
    file.close()
    ser.close()

# Retrieve data from sensor
def get_motion_data(ser):
    # Arduino sends in 1 bytes so read in first 8 bits, 
    # shifting them to the left and getting the next 8
    sensor_data = struct.unpack('b', ser.read())[0]
    sensor_data2 = struct.unpack('b', ser.read())[0]
    sensor_data3 = (sensor_data << 8) | sensor_data2

    print(sensor_data3)

    return sensor_data3


if __name__ == "__main__":
    main()
