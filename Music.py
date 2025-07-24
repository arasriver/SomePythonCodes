import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

# Initialize sounddevice
duration = 1.0
fs = 44100
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# Frequency parameters
f0 = 330  # main frequency
harmonics = [1, 2, 3]  # number of harmonics

# Generate the signal
signal = sum(np.sin(2 * np.pi * f0 * h * t) for h in harmonics)
signal = signal / np.max(np.abs(signal))

# Play the sound
sd.play(signal, samplerate=fs)
sd.wait()

# Plot the signal
plt.figure(figsize=(10, 4))
plt.plot(t[:1000], signal[:1000])
plt.title("Signal")
plt.xlabel("Time")
plt.ylabel("Domain")
plt.grid(True)
plt.show()
