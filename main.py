import json

def calculate_beats(bpm, song_duration):
    minutes = song_duration / 60
    total_beats = int(bpm * minutes)
    beat_interval = song_duration / total_beats

    beats = []
    for i in range(total_beats):
        beat_time = i * beat_interval
        beats.append(beat_time)

    return beats

def main():
    bpm = int(input("Enter the BPM: "))
    song_duration = int(input("Enter the song duration in seconds: "))

    beats = calculate_beats(bpm, song_duration)

    data = {
        "bpm": bpm,
        "song_duration": song_duration,
        "beats": beats
    }

    with open("output.json", "w") as file:
        json.dump(data, file)

    print("Beats calculated and saved in output.json.")

if __name__ == "__main__":
    main()
