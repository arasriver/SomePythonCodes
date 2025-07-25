import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

# Sampling parameters
fs = 44100
duration = 1.5
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# Extended note frequency table with sharps (#) and flats (b)
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

# Function to generate a chord signal from a list of notes
def generate_chord(notes):
    freqs = [note_freqs[n] for n in notes]
    signal = sum(np.sin(2 * np.pi * f * t) for f in freqs)
    signal /= np.max(np.abs(signal))  # Normalize
    return signal

# Get input from user and sanitize it
user_input = input("Enter 2 or 3 notes for the chord (e.g. C E G#): ").strip()
note_list = user_input.split()

# Validate input
invalid_notes = [n for n in note_list if n not in note_freqs]
if invalid_notes:
    print(f"Invalid notes: {', '.join(invalid_notes)}")
else:
    signal = generate_chord(note_list)
    sd.play(signal, samplerate=fs)
    sd.wait()

    # Plot waveform (zoom into the first 1000 samples)
    plt.figure(figsize=(10, 4))
    plt.plot(t[:1000], signal[:1000])
    plt.title(f"Waveform of the chord: {' - '.join(note_list)}")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
