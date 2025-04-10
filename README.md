![FFmpeg](https://img.shields.io/badge/Powered%20by-FFmpeg-orange.svg)
![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)
markdown
# Bilibili Video Merger Tool
Isang script para i-automate ang pagsasama ng audio at video mula sa Bilibili downloads, na may opsyon na mag-delete ng source files pagkatapos ng successful merge.

## Features
- Auto-detect ng 16/64 quality folders
- Title extraction mula sa `entry.json`
- Auto-delete ng source folder pagkatapos ng merge
- Compatible sa Termux (Android), Windows, at Linux

## Requirements
- Python 3.7+
- FFmpeg
- Folder structure mula sa Bilibili app:
download/
  ├── [ID1]/
  │   └── 1/
  │       ├── entry.json
  │       └── 16/ (o 64)
  │           ├── audio.m4s
  │           └── video.m4s
  ├── [ID2]/
  └── ...
## Installation

### Para sa Lahat ng Platform
1. **Install Python**:  
   [Python Official Site](https://www.python.org/downloads/)

2. **Install FFmpeg**:
   - **Termux**:
     ```bash
     pkg install python ffmpeg
     ```
   - **Windows**:  
     [FFmpeg Windows Builds](https://www.gyan.dev/ffmpeg/builds/)  
     (Ilagay sa system PATH)
   - **Linux**:
     ```bash
     sudo apt install python3 ffmpeg
     ```

## Usage

1. **I-download ang Script**:
   ```bash
   git clone https://github.com/yourusername/bilibili-merger.git
   cd bilibili-merger
   ```

2. **I-run ang Script**:
   ```bash
   python merger.py
   ```

3. **Input/Output Paths**:
   - **Default Input Path** (Para sa Bilibili Android):  
     `/storage/emulated/0/Android/data/com.bstar.intl/download/`
   - **Output Folder**:  
     Awtomatikong gagawa ng `Output/` folder sa current directory

4. **Auto-Delete Feature**:  
   Awtomatikong madi-delete ang source folder pagkatapos ng successful merge.

## Platform-Specific Guides

### 📱 Para sa Termux (Android)
1. Buksan ang Termux
2. I-enable ang storage access:
   ```bash
   termux-setup-storage
   ```
3. I-run ang script gamit ang default path:
   ```bash
   python merger.py
   ```

### 🖥️ Para sa Windows
1. I-double check na nasa PATH ang FFmpeg:
   ```cmd
   ffmpeg -version
   ```
2. Patakbuhin sa Command Prompt/Powershell:
   ```cmd
   python merger.py
   ```

### 🐧 Para sa Linux
1. Siguraduhing may write permission sa output folder
2. Gamitin ang terminal para i-run:
   ```bash
   python3 merger.py
   ```

## Troubleshooting
**Error: "FFmpeg not found"**  
- I-install ang FFmpeg at siguraduhing nasa system PATH

**Permission Denied**  
- Gamitin ang `sudo` sa Linux
- Bigyan ng storage permission ang Termux

**"Kulang ang audio/video"**  
- I-verify ang folder structure
- Tiyakin na may `audio.m4s` at `video.m4s`

## ⚠️ Mahalagang Paalala
- **Gumawa ng backup** bago i-run ang script
- Hindi irere-process ang mga nadelete nang folder
- Maaaring magkaiba ang quality depende sa source (16 = 360p, 64 = 720p)

---

*Ginawa para sa Bilibili video archival purposes. Gamitin ng may responsibilidad.*
```

---