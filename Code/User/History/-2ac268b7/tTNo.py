from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from playsound import playsound
text_prompt = """
Ok [sighs]
"""
preload_models()
audio_array = generate_audio(text_prompt)

# save audio to disk
write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)
playsound("bark_generation.wav")