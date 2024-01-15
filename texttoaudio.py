import torchaudio
import speechbrain as sb
from IPython.display import Audio
from speechbrain.dataio.dataio import read_audio
from speechbrain.pretrained import EncoderDecoderASR

# Change the current working directory if needed
# import os
# os.chdir("path/to/your/audio/files")

# Load the ASR model
asr_model = EncoderDecoderASR.from_hparams(source="speechbrain/asr-crdnn-rnnlm-librispeech", savedir="pretrained_models/asr-crdnn-rnnlm-librispeech")

# Transcribe the audio file
transcription = asr_model.transcribe_file('recorded_audio.wav')
print("Transcription:", transcription)

# Display the audio
signal = read_audio("recorded_audio.wav").squeeze()
Audio(signal, rate=16000)
