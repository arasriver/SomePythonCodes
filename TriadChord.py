import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

# Sampling parameters
fs = 44100
duration = 1.5
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# Extended frequency table with sharps (#) and flats (b)
note_freqs = {
    'C': 261.63,
    'C#': 277.18, 'Db': 277.18,
    'D': 293.66,
    'D#': 311.13, 'Eb': 311.13,
    'E': 329.63,
    'F': 349.23,
    'F#': 369.99, 'Gb': 369.99,
    'G': 392.00,
    'G#': 415.30, 'Ab': 415.30,
    'A': 440.00,
    'A#': 466.16, 'Bb': 466.16,
    'B': 493.88
}

# Function to generate a chord signal
def generate_chord(notes):
    freqs = [note_freqs[note] for note in notes]
    signal = sum(np.sin(2 * np.pi * f * t) for f in freqs)
    signal /= np.max(np.abs(signal))
    return signal

# Example: play A-C#-E (A major) or G-Bb-D (G minor)
chord_notes = ['G', 'Bb', 'D']

# Generate and play the chord
signal = generate_chord(chord_notes)
sd.play(signal, samplerate=fs)
sd.wait()

# Plot waveform (zoomed into the start)
plt.figure(figsize=(10, 4))
plt.plot(t[:1000], signal[:1000])
plt.title(f"Waveform of the chord {'-'.join(chord_notes)}")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()
