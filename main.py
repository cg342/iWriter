import argparse
from pathlib import Path

import speech_recognition as sr
from tqdm import tqdm


def main(args):
    input_path = Path(args.filepath)
    segment_length = args.segment_length * 1000

    output_path = Path("outputs") / (input_path.stem + ".txt")
    recognizer = sr.Recognizer()

    # outputtext = startConvertion(input_path,'zh')
    audio_segments = []
    with sr.AudioFile(input_path.as_posix()) as source:
        audio = recognizer.record(source)

        audio_length = int(source.FRAME_COUNT / source.SAMPLE_RATE) * 1000  # [ms]
        num_of_segments = audio_length // segment_length
        for i in range(num_of_segments):
            # partition each 30sec
            audio_segments.append(
                audio.get_segment(i * segment_length, (i + 1) * segment_length)
            )

        # process the last segment (<30 sec)
        if audio_length % segment_length:
            pass

    # Speech recognition by segments
    results = ""
    try:
        for audio_segment in tqdm(audio_segments):
            results += recognizer.recognize_google(audio_segment, language="zh")
    except sr.UnknownValueError:
        print("Google SR could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google SR; {0}".format(e))

    with open(output_path, "w") as f:
        f.write(results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Eng audio file to Chinese")
    parser.add_argument("-f", "--filepath", type=str, help="Path to file")
    parser.add_argument(
        "-l", "--segment_length", type=int, default=10, help="Length of segments in s"
    )

    args = parser.parse_args()
    main(args)
