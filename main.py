# import wave
import simpleaudio as sa
# import soundfile as sf
import numpy as np
# import librosa
import librosa.display
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # filePath = "WAV_Files/snare.wav"
    # filePath = "WAV_Files/I'd Do Anything - Simple Plan.wav"
    # filePath = "WAV_Files/Yura Yura - GReeeeN.wav"
    filePath = "WAV_Files/Welcome To The Black Parade - My Chemical Romance.wav"

    # with wave.open('WAV_Files/snare.wav') as w:
        # print(w.readframes(w.getnframes()).hex())
        # print(w.getnframes())
    # data, samplerate = sf.read(filePath)

    # print(samplerate)
    # print(data)

    # wave_obj = sa.WaveObject.from_wave_file(filePath)
    # play_obj = wave_obj.play()
    # play_obj.wait_done()

    y, sr = librosa.load(filePath, offset=240, duration=10)
    fig, ax = plt.subplots(nrows=1)
    y_perc = librosa.effects.percussive(y, margin=2)

    tempo, beat_frames = librosa.beat.beat_track(y=y_perc, sr=sr)
    print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    # print(beat_times)

    librosa.display.waveplot(y_perc, sr=sr, color='r', alpha=0.5)
    ax.set(title='Percussive')

    plt.show()

    y_perc *= 32767 / max(abs(y_perc))
    y_perc = y_perc.astype(np.int16)

    play_obj = sa.play_buffer(y_perc, 1, 2, sr)
    # wave_obj = sa.WaveObject.from_wave_file(filePath)
    # play_obj = wave_obj.play()

    play_obj.wait_done()
