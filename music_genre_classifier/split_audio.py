import librosa
import soundfile as sf
import argparse

# Function to split audio
def split_audio(file_path, segment_duration, genre, count_from):
    # Load audio file
    y, sr = librosa.load(file_path)

    # Calculate samples per segment
    samples_per_segment = int(segment_duration * sr)

    # Split audio into segments
    segments = []
    for start in range(0, len(y), samples_per_segment):
        end = start + samples_per_segment
        segment = y[start:end]
        segments.append(segment)

    # Save each segment
    for i, segment in enumerate(segments):
        output_file = f'{genre}.{str((count_from + i)).zfill(5)}.wav'
        sf.write(output_file, segment, sr)
        print(f"Segment {i+1} saved as {output_file}")

# Setup argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split audio file into segments")
    parser.add_argument("file_path", type=str, help="Path to the input audio file")
    parser.add_argument("segment_duration", type=int, help="Duration of each segment in seconds")
    parser.add_argument("genre", type=str, help="Music Genre")
    parser.add_argument("count_from", type=int, help="Count starts from this number")
    
    args = parser.parse_args()
    
    split_audio(args.file_path, args.segment_duration, args.genre, args.count_from)
