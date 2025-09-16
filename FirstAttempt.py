# -- My First Attempt using Python --

# 1. INPUT DATA
# Define an initial signal represented as a list of measurements in volts.
# This list simulates a sensor's output and includes invalid values
# (e.g., negative numbers or values above a certain threshold).

measurements = [1.2, 1.5, -0.5, 1.6, 8.5, 1.1, 1.8, 9.1, -1.2, 1.4]

# 2.PROCESSING FUNCTION.
# We will create a function so the code stays reusable and tidy.

def processing(volts, threshold):

   """Analyzes a list of measurements in volts.
   This function filters out invalid values (negative or above a given threshold),
   converts the valid measurements to millivolts (mV), and returns a new list 
   containing only the processed, valid data."""

   # We create an empty list so I can save the results later. 
   correctMeasurements = []

   # We have to use a 'for' loop to check every measurement from the input list.
   for v in volts:
      # We have to use an 'if' conditional to select if the measurement is correct or not.
      if 0 < v < threshold:
         # If it is correct, we have to convert it to milivolts and add it to the new list.
         mv = v*1000
         correctMeasurements.append(mv)
      else:
         # If it is wrong, we print a message to let us know.
         print(f"Eliminating wrong value: {v} V")

   # At the end of the function, it will show us the results.
   return correctMeasurements

# 3.SCRIPT EXECUTION
print("Starting measurement analysis...")

# We call our function and send it the data and the threshold value
validMeasurements = processing(measurements, 5.0)

print("Analysis finished")
print(f"Valid Measurements (mV): {validMeasurements}")