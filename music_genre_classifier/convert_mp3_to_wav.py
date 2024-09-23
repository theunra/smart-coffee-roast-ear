import argparse
from pydub import AudioSegment

# Function to convert mp3 to wav
def convert_mp3_to_wav(mp3_path, wav_path):
    # Load the MP3 file
    audio = AudioSegment.from_mp3(mp3_path)
    
    # Export the audio as a WAV file
    audio.export(wav_path, format="wav")
    print(f"Converted {mp3_path} to {wav_path}")

# Setup argument parsing
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert MP3 to WAV")
    parser.add_argument("mp3_path", type=str, help="Path to the input MP3 file")
    parser.add_argument("wav_path", type=str, help="Path to the output WAV file")

    args = parser.parse_args()
    
    # Call the conversion function with the provided arguments
    convert_mp3_to_wav(args.mp3_path, args.wav_path)
