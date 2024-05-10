import sounddevice
from scipy.io.wavfile import write
fs=44100 # Sample rate
seconds=10 # Duration of recording
print("Recording...")

record_voice=sounddevice.rec(int(seconds*fs), samplerate=fs, channels=2)
sounddevice.wait()
write("output.wav", fs, record_voice)