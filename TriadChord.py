import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

# Sampling rate and duration
fs = 44100  # 44.1 kHz standard sampling rate
duration = 1.5  # seconds
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# Frequency table for basic notes (in Hz)
note_freqs = {
    'C': 261.63,
    'D': 293.66,
    'E': 329.63,
    'F': 349.23,
    'G': 392.00,
    'A': 440.00,
    'B': 493.88
}

# Function to generate a chord signal from a list of notes
def generate_chord(notes):
    freqs = [note_freqs[note.upper()] for note in notes]  # convert note names to frequencies
    signal = sum(np.sin(2 * np.pi * f * t) for f in freqs)  # sum the sine waves
    signal /= np.max(np.abs(signal))  # normalize to prevent clipping
    return signal

# Choose the chord you want to play
chord_notes = ['C', 'C', 'C']  # E minor triad

# Generate the signal and play it
signal = generate_chord(chord_notes)
sd.play(signal, samplerate=fs)
sd.wait()

# Plot the waveform (just the beginning part for clarity)
plt.figure(figsize=(10, 4))
plt.plot(t[:1000], signal[:1000])
plt.title(f"Waveform of the chord {'-'.join(chord_notes)}")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()
