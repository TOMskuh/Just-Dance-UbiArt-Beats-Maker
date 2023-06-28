import os
import json

def calculate_beats(bpm, song_duration):
    minutes = song_duration / 60
    total_beats = int(bpm * minutes)
    beat_interval = song_duration * 1000 / total_beats

    beats = []
    for i in range(total_beats):
        beat_time = int(i * beat_interval)
        beats.append(beat_time)

    return beats

def main():
    print("Welcome to Yukii's Beat Generator for Just Dance")
    codename = input("Enter the codename for the output file: ")
    bpm = int(input("Enter the BPM: "))
    song_duration = int(input("Enter the song duration in seconds: "))

    beats = calculate_beats(bpm, song_duration)

    folder_path = f"output/{codename.lower()}"
    os.makedirs(folder_path, exist_ok=True)
    filename = f"{folder_path}/{codename.lower()}_beats.json"

    data = {
        "codename": codename,
        "bpm": bpm,
        "song_duration": song_duration,
        "beats": beats
    }

    with open(filename, "w") as file:
        json.dump(data, file)

    print(f"Beats calculated and saved in {filename}.")

if __name__ == "__main__":
    main()
