import os
import json
import subprocess
import re
import shutil  # Idinagdag para sa folder deletion

def sanitize_filename(title):
    """I-sanitize ang title para maging valid na filename"""
    return re.sub(r'[\\/*?:"<>|]', "_", title)

def merge_audio_video(root_folder, output_folder):
    # I-traverse ang root folder
    for id_folder in os.listdir(root_folder):
        id_path = os.path.join(root_folder, id_folder)
        
        if not os.path.isdir(id_path):
            continue

        # Hanapin ang '1' na subfolder
        one_folder = os.path.join(id_path, "1")
        if not os.path.exists(one_folder):
            continue

        try:
            # Basahin ang entry.json
            entry_json = os.path.join(one_folder, "entry.json")
            with open(entry_json, 'r', encoding='utf-8') as f:
                entry_data = json.load(f)
                title = entry_data.get("title", "untitled")
        except:
            title = "untitled"

        # I-sanitize ang title
        clean_title = sanitize_filename(title)
        output_path = os.path.join(output_folder, f"{clean_title}.mp4")

        # Hanapin ang 16/64 na folder
        stream_folder = None
        for res in ["16", "64"]:
            temp_path = os.path.join(one_folder, res)
            if os.path.exists(temp_path):
                stream_folder = temp_path
                break

        if not stream_folder:
            print(f"Walang 16/64 folder sa {one_folder}")
            continue

        # Hanapin ang audio at video files
        audio_file = os.path.join(stream_folder, "audio.m4s")
        video_file = os.path.join(stream_folder, "video.m4s")

        if not all([os.path.exists(audio_file), os.path.exists(video_file)]):
            print(f"Kulang ang audio/video sa {stream_folder}")
            continue

        # FFmpeg command para pagsamahin
        command = [
            'ffmpeg',
            '-i', video_file,
            '-i', audio_file,
            '-c:v', 'copy',
            '-c:a', 'aac',
            '-strict', 'experimental',
            output_path
        ]

        # I-run ang command at mag-delete pag successful
        try:
            subprocess.run(command, check=True)
            print(f"Success: {clean_title}")
            
            # Delete ang buong ID folder pagkatapos ng successful merge
            try:
                shutil.rmtree(id_path)
                print(f"Na-delete na ang source folder: {id_path}")
            except Exception as delete_error:
                print(f"Hindi na-delete ang {id_path}: {str(delete_error)}")

        except subprocess.CalledProcessError as e:
            print(f"Error sa {clean_title}: {e}")

if __name__ == "__main__":
    input_folder = "/storage/emulated/0/Android/data/com.bstar.intl/download/"
    output_folder = "Output/"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    merge_audio_video(input_folder, output_folder)