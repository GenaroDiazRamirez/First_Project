# -- My First Attempt using Python --

# 1.INPUT DATA.
# I am going to introduce random values from a fake sensor, 
# an initial signal expressed as a list of measurements in volts.
# This list contains wrong values, as negative inputs or higher values.

measurements = [1.2, 1.5, -0.5, 1.6, 8.5, 1.1, 1.8, 9.1, -1.2, 1.4]

# 2.PROCESSING FUNCTION.
# I will create a function so the code stays reusable and tidy.

def processing(volts, threshold):

   # This function will: 
   # - Analys the list of measurements in volts.
   # - Filter incorrect values (negative or above a threshold).
   # Converts valid values to millivolts (mV).
   # Returns a list with the processed values.

   # I create an empty list so I can save the results later. 
   correctMeasurements = []

   # We have to use a 'for' loop to check every measurement from the input list.
   for v in volts:
      # We have to use an 'if' conditional to select if the measurement is correct or not.
      if 0 < v < threshold
      # If it is correct, we have to convert it to milivolts and add it to the new list.
      mv = v*1000
      correctMeasurements.append(mv)
      else
      # If it is wrong, we print a message to let us know.
      print(f"Eliminating wrong value: {v} V")

   # At the end of the function, it will show us the results.
   return correctMeasurements
