# FLAC to ALAC Converter

This Python program converts FLAC audio files to ALAC (Apple Lossless Audio Codec) format while maintaining all the metadata and original album art.

## Features
- Converts `.flac` files to `.m4a` (ALAC) format.
- Preserves metadata and album art during conversion.
- Maintains the original folder structure in the destination directory.

## Requirements
To run this program, you need to have Python 3 and FFmpeg installed on your system.

### Installing FFmpeg

#### Windows
1. Download the FFmpeg build from [FFmpeg official website](https://ffmpeg.org/download.html).
2. Extract the downloaded zip file.
3. Add the `bin` folder (inside the extracted folder) to your system's PATH environment variable.

#### macOS
You can install FFmpeg using Homebrew. Open your terminal and run:
```bsh
brew install ffmpeg
```

#### Linux
You can install FFmpeg using your package manager. For example, on Ubuntu, run:
```bash
sudo apt update
sudo apt install ffmpeg
```

## Usage

1. Update the `parent_directory` and `destination_directory` paths in the `main.py` file:
parent_directory = '/mnt/e/music' # Replace with your FLAC files directory
destination_directory = '/mnt/e/music-alac' # Replace with your desired ALAC output directory

2. Run the program using Python 3:
```bash
python3 main.py
```

Alternatively, you can use:
```bash
python main.py
```

## Notes
- The program will walk through the specified `parent_directory`, convert all `.flac` files to ALAC format, and save them in the specified `destination_directory`, preserving the folder structure.
- Other file types found in the parent directory will be copied to the destination without modification.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
