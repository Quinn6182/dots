from TTS.tts.configs.bark_config import BarkConfig
from TTS.tts.models.bark import Bark
import scipy

config = BarkConfig()
model = Bark.init_from_config(config)
model.load_checkpoint(config, checkpoint_dir="bark/", eval=True)
text = "this is an attempt at voice cloning"
output_dict = model.synthesize(text, config, speaker_id="speaker", voice_dirs="bark_voices/")
sample_rate=24000
scipy.io.wavfile.write("out.wav", rate=sample_rate, data=output_dict["wav"])