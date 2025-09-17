# -- NumPy Signal Simulation --

import numpy as np
import matplotlib.pyplot as plt

# 1. SIGNAL PARAMETERS
# Define the parameters for a simulated signal.
samplingRate = 1000   # samples per second
duration = 2          # seconds 
frequency = 5         # cycles per second (Hz)

# 2. GENERATE THE TIME VECTOR
# Create a time array from 0 to 'duration' with the correct number of points.
# The number of points is the samplingRate times the duration.
numPoints = samplingRate*duration
time = np.linspace(0,duration,numPoints)

# 3. CREATE A SINE WAVE
# Generate a sine wave using 'np.sin()' function.
sineSignal = np.sin(2*np.pi*frequency*time)

# 4. ADD NOISE
# Generate random noise to add to the signal.
# 'np.random.noise' creates noise from a normal (Gaussian) distribution.
# This function uses a scale parameter that controls the amplitude of the noise.
noise = np.random.normal(scale = 0.5, size = numPoints)
noisySignal = sineSignal+noise

# 5. VISUALIZATION
print("Plotting the signals...")

# Create a figure and axes for the plot.
# 'figsize' controls the window size.
plt.figure(figsize = (12,6))

# Plot the original signal and the noisy one to compare.
plt.plot(time, noisySignal, label = 'Noisy Signal')
plt.plot(time, sineSignal, label = 'Original Signal', linestyle = '--')

plt.title('Simulated Sine Wave Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.legend()                              # Display the legend
plt.grid(True)                            # Add a grid for easier reading

# Display the plot window.
plt.show()

# 6. BASIC ANALYSIS
print("Performing basic signal analysis with NumPy...")

# Calculate statistics of the noisy signal using built-in methods.
# These operations are v faster than standar Python loops.
mean = noisySignal.mean() 
max = noisySignal.max()
min = noisySignal.min()

# Print the values extracted from the analysis.
# .4f formats to 4 decimal places.
print(f"Mean of the signal: {mean:.4f}") 
print(f"Max value of the signal: {max:.4f}")
print(f"Min value of the signal: {min:.4f}")

# Filter the signal to find all data points above a certain amplitude.
# Use boolean indexing here.
highPoints = noisySignal[noisySignal > 2]
print(f"Found {len(highPoints)} data points with amplitude over 2 V")