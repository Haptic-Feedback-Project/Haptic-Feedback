from array import *

# Class to store data collected from a sensor
class Motion_data:

    def __init__(self, i, j, k, phi, theta, psi):
      
      # initalize data
      self.i = []
      self.j = []
      self.k = []
      self.phi = []
      self.theta = []
      self.psi = []
      
     
def main():

    # Initialize 
    counter = 0
    
    sensor_array = [new Motion_data(), new Motion_data(), new Motion_data(),
    new Motion_data(), new Motion_data(), new Motion_data()]


    # Set the bias noise for all sensors (May need to be unique to each sensor) 
    BIAS_NOISE = 123
    
    #Set how many instances of data we will store
    MAX_DATA_SIZE = 500
    
    # Initialize position of sensors(constant, depends on sensor), need something that contains position of sensor
    
    # Calibrate sensor orientation
    
    # Constantly collect data
    while(1):
    
    """
    get 6 data items from arduino
    access each corresponding data point of each sensor
    change that data location to the new data    
    """
    
      walking = 0
      turning = 0
      swaying = 0
     
 

      # Fill in motion data for each sensor at counter index
      get_motion_data(sensor_array, counter)
      counter = (counter + 1) % MAX_DATA_SIZE
     

      # Check for white noise data(are we walking or turning?) Will return 0 for false or 1 for true
      walking = check_walking(sensor_array)
      turning = check_turning(sensor_array)

      if walking && turning:
        # Check for sway, either ignoring variables for walking and turning, 
        # or expect a different tolerance threshold

        # If sway threshold is met
        swaying = 1
      else if walking:
        # Check for sway, either ignoring variables for walking, 
        # or expect a different tolerance threshold

        # If sway threshold is met
        swaying = 1
      else if turning:
        # Check for sway, either ignoring variables for turning, 
        # or expect a different tolerance threshold

        # If sway threshold is met
        swaying = 1
      else: # Just standing   
        # Check for sway, either ignoring variables for turning, 
        # or expect a different tolerance threshold

        # If sway threshold is met
        swaying = 1   

      if swaying:
        # Determine which devices to send force to, and how much
        haptic_device_array = initialize_haptic_devices(sensor_array, threshhold) 

        # Respond with how much pressure to send on which devices
        send_pressure(haptic_device_array);  

def get_motion_data(sensor_array, counter):
  # Request data from board/sensors

  # Initialize class info?

def check_walking(sensor_array):
  walking = 0
  # Perform calculations that determines whether we are in walking state

  # If we are return walking = 1

  return walking

def check_turning(sensor_array):
  turning = 0
  # Perform calculations that determines whether we are in turning state

  # If we are return turning = 1

  return turning

def initialize_haptic_devices(sensor_array, threshhold): 
  haptic_device_array = array('f',[ 0, 0, 0, 0, 0, 0 ])

  # Determine which pressure points to trigger and with how much force

  # Each index of the array corresponds with with a haptic feedback device,
  # The value is how much pressure to apply
  return haptic_device_array

def send_pressure(haptic_device_array):
  # Send the array to Arduino/haptic devices

  # Will require some sort of struct

if __name__ == "__main__":
    main()
