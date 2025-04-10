![FFmpeg](https://img.shields.io/badge/Powered%20by-FFmpeg-orange.svg)
![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)

# Bilibili Video Extractor Tool

A script to automate merging audio and video from Bilibili Android downloads, with auto-delete feature for processed files.

## Features
- Auto-detect 16/64 quality folders
- Title extraction from `entry.json`
- Auto-delete source folder after merge
- Optimized for Termux (Android)

## Requirements
- Android device with Termux
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

### Termux Setup
1. Update packages:
   ```bash
   pkg update && pkg upgrade
   ```

2. Install dependencies:
   ```bash
   pkg install python ffmpeg git
   ```

3. Clone repository:
   ```bash
   git clone https://github.com/CyberArcenal/bili_video_extractor.git
   cd bili_video_extractor
   ```

## Usage

1. Grant storage access:
   ```bash
   termux-setup-storage
   ```

2. Run the script:
   ```bash
   python merger.py
   ```

3. Default paths:
   - Input: `/storage/emulated/0/Android/data/com.bstar.intl/download/`
   - Output: `Output/` folder in current directory

4. Processed folders will be automatically deleted

## Troubleshooting
**Error: "FFmpeg not found"**  
- Reinstall FFmpeg: `pkg reinstall ffmpeg`

**Permission Denied**  
- Grant storage permission in Termux
- Restart Termux after permission grant

**"Missing audio/video"**  
- Verify Bilibili download completed
- Check folder structure matches requirements

## ⚠️ Important Notes
- Backup files before first use
- Internet connection required for initial setup
- Test with 1-2 files first before bulk processing

---

*For Bilibili Android users only. Not affiliated with Bilibili Inc.*