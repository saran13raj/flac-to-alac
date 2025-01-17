import os
import subprocess
import shutil
from pathlib import Path
import datetime

# log_file_path = 'error_log.txt'

def convert_flac_to_alac(parent_dir, destination_dir):
    # Ensure the destination directory exists
    Path(destination_dir).mkdir(parents=True, exist_ok=True)

    # Walk through the parent directory
    for root, dirs, files in os.walk(parent_dir):
        for file in files:
            # Construct the full path of the current file
            current_file_path = os.path.join(root, file)

            # Create the relative path to maintain folder structure
            relative_path = os.path.relpath(root, parent_dir)
            destination_folder = os.path.join(destination_dir, relative_path)

            # Ensure the destination folder exists
            Path(destination_folder).mkdir(parents=True, exist_ok=True)

            if file.endswith('.flac'):
                # Construct the output ALAC file path
                alac_file_path = os.path.join(destination_folder, f"{Path(file).stem}.m4a")

                # Convert FLAC to ALAC using ffmpeg
                subprocess.run(['ffmpeg', '-i', current_file_path, '-codec', 'copy', '-acodec', 'alac', alac_file_path], check=True)
            else:
                # For other file types, just copy them to the destination
                destination_file_path = os.path.join(destination_folder, file)
                shutil.copy(current_file_path, destination_file_path)  # Use copy to duplicate the file


# Example usage:
parent_directory = '/mnt/e/music'  # Replace with your FLAC files directory
destination_directory = '/mnt/e/music-alac'  # Replace with your desired ALAC output directory

convert_flac_to_alac(parent_directory, destination_directory)
