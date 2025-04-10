![FFmpeg](https://img.shields.io/badge/Powered%20by-FFmpeg-orange.svg)
![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)

# Bilibili Video Extractor Tool

A script to automate merging audio and video from Bilibili downloads, with an option to delete source files after successful merge.

## Features
- Auto-detect 16/64 quality folders
- Title extraction from `entry.json`
- Auto-delete source folder after merge
- Compatible with Termux (Android), Windows, and Linux

## Requirements
- Python 3.7+
- FFmpeg
- Bilibili app folder structure:
  ```
  download/
  ├── [ID1]/
  │   └── 1/
  │       ├── entry.json
  │       └── 16/ (or 64)
  │           ├── audio.m4s
  │           └── video.m4s
  ├── [ID2]/
  └── ...
  ```

## Installation

### For All Platforms
1. **Install Python**:  
   [Python Official Site](https://www.python.org/downloads/)

2. **Install FFmpeg**:
   - **Termux**:
     ```bash
     pkg install python ffmpeg
     ```
   - **Windows**:  
     [FFmpeg Windows Builds](https://www.gyan.dev/ffmpeg/builds/)  
     (Add to system PATH)
   - **Linux**:
     ```bash
     sudo apt install python3 ffmpeg
     ```

## Usage

1. **Download the Script**:
   ```bash
   git clone https://github.com/CyberArcenal/bili_video_extractor.git
   cd bili_video_extractor
   ```

2. **Run the Script**:
   ```bash
   python merger.py
   ```

3. **Input/Output Paths**:
   - **Default Input Path** (For Bilibili Android):  
     `/storage/emulated/0/Android/data/com.bstar.intl/download/`
   - **Output Folder**:  
     Automatically creates `Output/` folder in current directory

4. **Auto-Delete Feature**:  
   Source folders will be automatically deleted after successful merge.

## Platform-Specific Guides

### 📱 For Termux (Android)
1. Open Termux
2. Enable storage access:
   ```bash
   termux-setup-storage
   ```
3. Run script using default path:
   ```bash
   python merger.py
   ```

## Troubleshooting
**Error: "FFmpeg not found"**  
- Install FFmpeg and ensure it's in system PATH

**Permission Denied**  
- Use `sudo` on Linux
- Grant storage permission in Termux

**"Missing audio/video"**  
- Verify folder structure
- Ensure `audio.m4s` and `video.m4s` exist

## ⚠️ Important Notes
- **Create backups** before running the script
- Already deleted folders won't be reprocessed
- Quality may vary by source (16 = 360p, 64 = 720p)

---

*Created for Bilibili video archival purposes. Use responsibly.*
