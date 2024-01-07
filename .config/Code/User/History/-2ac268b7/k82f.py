from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from playsound import playsound
# download and load all models
preload_models()

# generate audio from text
text_prompt = """
    last even show would public keep lead say open at we after problem look need what small open most group or open lead never here
"""
audio_array = generate_audio(text_prompt)

# save audio to disk
write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)
playsound("bark_generation.wav")