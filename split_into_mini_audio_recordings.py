from moviepy.editor import *
from pydub import AudioSegment


def split_into_mini_audio_recordings(sound, silence_threshold=-45.0, step_size=10):   # silence_threshold=-45.0 - unique to each audio recording
    samples_count = 0
    silence_ms = 0
    step_size_for_pause = 500
    assert step_size > 0

    while samples_count < 16:   # number of samples you need from output

        while sound[silence_ms:silence_ms + step_size].dBFS < silence_threshold and silence_ms < len(sound):
            silence_ms += step_size

        start = silence_ms
        i = 1
        while sound[start + step_size_for_pause*i:start + step_size_for_pause*i + step_size_for_pause].dBFS > silence_threshold:
            end = start + step_size_for_pause*i
            i += 1

        samples_count += 1

        end = start + step_size_for_pause * i
        audio = sound[start:end]
        str = "A:/Downloads/dataset/output_audio_{}.wav".format(samples_count)
        audio.export(str, format="wav")   # saving

        silence_ms = end
    return


audio_original = AudioFileClip("A:/Downloads/360p.mp4")
audio_original.write_audiofile("A:/Downloads/original_audio.wav")   # saving
sound = AudioSegment.from_file("A:/Downloads/original_audio.wav", format="wav")

split_into_mini_audio_recordings(sound)
