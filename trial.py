""" import wave
obj=wave.open("Conference.wav","rb")
print("channels",obj.getnchannels())
print("width",obj.getsampwidth())
print("frame rate",obj.getframerate())
print("frame number",obj.getnframes())
print("parameters",obj.getparams()) """

""" import wave
import matplotlib.pyplot as plt
import numpy as np

obj=wave.open("Conference.wav","rb")
sample_freq=obj.getframerate()
n_sample=obj.getnframes()
signal_wave=obj.readframes(-1)

obj.close()

t_audio=n_sample/sample_freq

print(t_audio)

signal_array=np.frombuffer(signal_wave, dtype=np.int16)

times=np.linspace(0,t_audio,num=n_sample)

plt.figure(figsize=(15,5))
plt.plot(times,signal_array)
plt.title("audio")
plt.ylabel("signal wave")
plt.xlabel("time(s)")
plt.xlim(0,t_audio)
plt.show()

 """

import pyaudio
import wave
FRAMES_PER_BUFFER=3200
FORMAT=pyaudio.paInt16
CHANNEL=1
RATE=16000

p=pyaudio.PyAudio()

stream=p.open(
    format=FORMAT,
    channels=CHANNEL,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER
)

print("start recording")
seconds=5
frames=[]
for i in range(0,int(RATE/FRAMES_PER_BUFFER*seconds)):
    data=stream.read(FRAMES_PER_BUFFER)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

obj=wave.open("output.wav","wb")
obj.setnchannels(CHANNEL)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.setframerate(RATE)
obj.writeframes(b"".join(frames))
obj.close()
