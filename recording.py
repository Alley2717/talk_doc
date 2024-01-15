""" import sounddevice as sd
from scipy.io.wavfile import write

def record_and_save(filename, duration=5, samplerate=44100):
    print(f"Recording {duration} seconds of audio...")
    
    # Record audio
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()  # Wait for the recording to finish
    
    # Save audio to a .wav file
    write(filename, samplerate, audio_data)
    
    print(f"Audio saved as {filename}")

# Example usage:
output_filename = "recorded_audio.wav"
record_and_save(output_filename, duration=5)
 """

import sounddevice as sd
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import numpy as np

def record_and_save_with_plot(filename, duration=5, samplerate=44100):
    print(f"Recording {duration} seconds of audio...")
    
    # Record audio
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()  # Wait for the recording to finish
    
    # Save audio to a .wav file
    write(filename, samplerate, audio_data)
    
    print(f"Audio saved as {filename}")

    # Generate and plot the waveform
    time = np.arange(0, len(audio_data)) / samplerate
    plt.figure(figsize=(10, 4))
    plt.plot(time, audio_data[:, 0], label='Channel 1')
    plt.plot(time, audio_data[:, 1], label='Channel 2')
    plt.title('Audio Waveform')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)
    plt.savefig('audio_waveform.png')
    plt.show()

# Example usage:
output_filename = "recorded_audio.wav"
record_and_save_with_plot(output_filename, duration=5)
