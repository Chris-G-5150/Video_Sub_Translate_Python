# Video Sub Translate 🎙️➡️🌍

**Video Sub Translate** is a speech processing pipeline that takes in video or audio, removes silence, transcribes speech using [Faster-Whisper](https://github.com/guillaumekln/faster-whisper), and prepares the results for translation and subtitle generation (SRT).

It’s designed to handle real-world media efficiently — cutting silence first means less audio to process, faster transcription, and cleaner subtitles.

---

## ✨ Features
- 🎬 **Video/Audio input** (via [PyDub](https://github.com/jiaaro/pydub))  
- 🔇 **Silence removal** for faster processing & clean chunks  
- 🧩 **SpeechChunk abstraction** — each chunk carries its transcription, metadata, and timing offsets  
- ⚡ **GPU-accelerated transcription** (Faster-Whisper on CUDA)  
- 🌍 **Dynamic language support** (auto-detect or user-specified)  
- 📝 **Per-chunk text output** for debugging / translation pipelines  
- ⏱️ **SRT subtitle export** aligned to the original timeline (video-editor ready)  

---

## 🛠️ Tech Stack
- **Python 3.10+**
- [PyDub](https://github.com/jiaaro/pydub) — audio cutting & silence removal  
- [Faster-Whisper](https://github.com/guillaumekln/faster-whisper) — transcription  
- **CUDA + cuDNN** — GPU acceleration  
- [GPUtil](https://github.com/anderskm/gputil) — GPU checks  

---

## 🚀 Architecture Overview

```mermaid
flowchart TD
    A[Video/Audio Input] --> B[Silence Removal (PyDub)]
    B --> C[SpeechChunks Created]
    C --> D[Transcription (Faster-Whisper)]
    D --> E[Per-Chunk .txt Files]
    D --> F[Merge with Offsets]
    F --> G[SRT Subtitle Output]
    E --> H[Optional Translation Pipeline]
    H --> G
```

---

## 🚀 Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Place your media file in the `input/` directory.  

3. Run the main script:
   ```bash
   python main.py
   ```

4. Results:
   - Per-chunk `.txt` files → `output/transcriptions/`  
   - Final `.srt` file → aligned to the original video timeline  

---

## ⚡ Example (console output)

```
🎙️ Processing chunk 3/12: chunks/clip_3.wav
   Detected language: en
   [00:01.20s -> 00:04.10s] Hello, how are you?
   [00:04.10s -> 00:07.50s] I'm fine, thanks.
```

---

## 💡 Why SpeechChunks?
Silence removal splits long recordings into manageable `SpeechChunk`s.  
Each chunk stores:
- start / end offsets (ms) in the original video,  
- transcription text,  
- source language,  
- file paths for disk output.  

This makes it easy to:
- process efficiently,  
- debug per-chunk results,  
- reassemble accurate subtitles later.  

---

## 🏗️ Future Work
- 🌍 Automatic translation step (integrate with e.g. MarianMT, DeepL, or OpenAI API)  
- 🗂️ Project-wide config for transcription options (beam size, temperature, language)  
- 🖥️ Web UI for uploading media and downloading subtitles  

---

## 👨‍💻 About
This project was built as a way to:
- Explore large-scale speech processing  
- Get hands-on with CUDA & Whisper internals  
- Demonstrate resilience in debugging complex data pipelines

---

### 🔜 Features to Implement
- **Text File Export:** Write transcriptions to disk in a translation-ready format.  
- **Event System:** Introduce hooks/events for modular extension (e.g. monitoring, logging, UI updates).  
- **Translation Pipeline:** Add input/output translation into any supported language.  
- **Subtitle Generation:** Build SRT/Subtitle files with precise timecodes for use in video editors.  
- **Web UI:** Provide a simple, interactive interface for end users.  

---

### 📌 Notes on Progress
- The core AI transcription pipeline is **fully functional** and producing highly accurate subtitles.  
- Stress-tested on **challenging, noisy audio** (e.g. old TV shows with poor sound quality).  
- Whisper/Faster-Whisper can handle a wide variety of accents — including **UK regional dialects** (yes, even 1980s *Coronation Street*).  
- Debugging is ongoing across the full pipeline, but the results so far are extremely promising.  

---

## 👨‍💻 About the Developer  
This project was built as part of a portfolio to demonstrate:  
- Persistence and resilience in solving complex technical challenges.  
- Strong problem-solving ability across Python, PyTorch, and CUDA.  
- End-to-end system design, from data preprocessing to AI inference to output formatting.  

> It reflects a commitment to building practical, production-ready AI solutions under real-world constraints.  

