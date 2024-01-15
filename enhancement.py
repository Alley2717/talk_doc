""" from speechbrain.pretrained import SepformerSeparation as separator
import torchaudio
from pathlib import Path  # Import Path for handling file paths
import os

# Load the pre-trained Sepformer model for audio source separation
model = separator.from_hparams(source="speechbrain/sepformer-whamr-enhancement", savedir='pretrained_models/sepformer-whamr-enhancement')

# Provide the actual path to the audio file you want to process
input_audio_path = torchaudio.load(os.fspath('example_whamr.wav'))# Assuming 'Conference.wav' is in the current directory

# Convert the PosixPath object to a string using str()
input_audio_path_str = str(Path(input_audio_path))

# Perform audio source separation
est_sources = model.separate_file(path=input_audio_path_str)
string=str(est_sources)
# Save the separated sources
torchaudio.save("enhanced_whamr.wav", string[:, :, 0].detach().cpu(), 8000)

 """
""" from speechbrain.pretrained import SepformerSeparation as separator
import torchaudio
from pathlib import Path  # Import Path for handling file paths

# Load the pre-trained Sepformer model for audio source separation
model = separator.from_hparams(source="speechbrain/sepformer-whamr-enhancement", savedir='pretrained_models/sepformer-whamr-enhancement')

# Provide the actual path to the audio file you want to process
input_audio_path = 'audio_cache/example_whamr.wav'  # Assuming 'example_whamr.wav' is in the current directory
input_audio, _ = torchaudio.load(input_audio_path)

# Perform audio source separation
est_sources = model.separate_batch(input_audio)

# Save the separated sources
torchaudio.save("enhanced_whamr.wav", est_sources[0, :, :].detach().cpu(), 8000) """
from speechbrain.pretrained import SepformerSeparation as separator
import torchaudio

model = separator.from_hparams(source="speechbrain/sepformer-whamr-enhancement", savedir='pretrained_models/sepformer-whamr-enhancement')

# for custom file, change path
path='example_whamr.wav'
audio,_=torchaudio.load(path)
est_sources = model.separate_batch(audio) 

torchaudio.save("enhanced_whamr2.wav", est_sources[:, :, 0].detach().cpu(), 8000)
