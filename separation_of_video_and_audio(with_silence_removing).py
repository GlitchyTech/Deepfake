from moviepy.editor import *
from pydub import AudioSegment


def detect_leading_silence(sound, silence_threshold=-25.0, step_size=5):  # step_size [ms], silence_threshold [ms]
    silence_ms = 0

    assert step_size > 0
    while sound[silence_ms:silence_ms + step_size].dBFS < silence_threshold and silence_ms < len(sound):
        silence_ms += step_size

    return silence_ms


audio_original = AudioFileClip("A:/Downloads/360p.mp4")
audio_original.write_audiofile("A:/Downloads/original_audio.wav")   # saving
sound = AudioSegment.from_file("A:/Downloads/original_audio.wav", format="wav")

start_of_sound = detect_leading_silence(sound)
duration = len(sound)

trimmed_sound = sound[start_of_sound:duration]
trimmed_sound.export("A:/Downloads/output_audio.wav", format="wav")   # saving

video_new = VideoFileClip("A:/Downloads/360p.mp4").subclip(start_of_sound/1000, duration/1000)
video_new.write_videofile("A:/Downloads/output_video.mp4")   # saving

