# 🎬 AI Video Generation Pipeline

<p align="center">
  <strong>An automated pipeline for turning a topic into a complete AI-generated video.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white">
  <img src="https://img.shields.io/badge/MoviePy-000000?style=for-the-badge">
  <img src="https://img.shields.io/badge/Pexels-05A081?style=for-the-badge">
  <img src="https://img.shields.io/badge/gTTS-FF6F00?style=for-the-badge">
</p>

---

## 💡 Overview

**AI Video Generation Pipeline** is an automated Python workflow that takes a video topic and transforms it into the core assets required for a complete short-form video.

Instead of manually creating every part of a video, the pipeline connects multiple AI and media-generation steps into a single workflow.

### From:

> **Video Topic**

### To:

> **Script + Voiceover + Visuals + SEO Metadata + Thumbnail + Final Video**

---

## ⚡ Pipeline

~~~text
                 VIDEO TOPIC
                      │
                      ▼
             ┌─────────────────┐
             │  Script Creator │
             │  Google Gemini  │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │   Voiceover     │
             │      gTTS       │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │  Video Assets   │
             │     Pexels      │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Video Composer  │
             │    MoviePy      │
             └────────┬────────┘
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
 ┌─────────────────┐      ┌─────────────────┐
 │  SEO Metadata   │      │    Thumbnail    │
 │  Gemini + JSON  │      │     Pillow      │
 └─────────────────┘      └─────────────────┘
          │                       │
          └───────────┬───────────┘
                      ▼
              COMPLETE VIDEO
~~~

---

## ✨ Features

- 🤖 AI-generated video scripts using **Google Gemini**
- 🎙️ Automated voiceover generation
- 🎥 Automatic video asset retrieval
- ✂️ Automated video composition
- 🔍 AI-generated SEO metadata
- 🖼️ Automated thumbnail generation
- 📦 Organized output generation
- ⚙️ End-to-end Python workflow
- 🔐 API credentials handled through environment variables

---

## 🧠 How It Works

### 1. Script Generation

The pipeline sends the selected topic to Gemini and generates a structured video script.

~~~text
Topic
  ↓
Gemini
  ↓
Video Script
~~~

---

### 2. Voice Generation

The generated script is converted into a spoken voiceover using text-to-speech.

~~~text
Script
  ↓
Text-to-Speech
  ↓
Audio File
~~~

---

### 3. Visual Generation

Relevant video footage is retrieved and prepared as visual assets for the video.

~~~text
Video Topic
  ↓
Visual Search
  ↓
Video Clips
~~~

---

### 4. Video Composition

The generated voiceover and downloaded visual assets are combined into the final video using MoviePy.

~~~text
Video Clips
     +
Voiceover
     │
     ▼
  MoviePy
     │
     ▼
Final Video
~~~

---

### 5. SEO Metadata

Gemini is also used to generate metadata intended to help prepare the video for publishing.

This can include information such as:

- Title
- Description
- Tags
- Keywords

---

### 6. Thumbnail Generation

A thumbnail is generated as part of the automated production workflow.

~~~text
Video Topic
    ↓
Thumbnail Generation
    ↓
Thumbnail Image
~~~

---

## 🏗️ Project Structure

~~~text
AI-Video-Generation-Pipeline/
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
│
├── modules/
│   ├── script_generator.py
│   ├── seo_generator.py
│   ├── thumbnail_generator.py
│   ├── voice_generator.py
│   └── video_generator.py
│
├── assets/
│
├── output/
│
└── README.md
~~~

> Generated folders and filenames may vary depending on the project configuration and execution.

---

## 🛠️ Technology Stack

### AI

![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)

Used for:

- Script generation
- SEO metadata generation

### Video

![MoviePy](https://img.shields.io/badge/MoviePy-000000?style=for-the-badge)

Used for combining and processing video and audio assets.

### Voice

**gTTS**

Used to convert generated scripts into voiceover audio.

### Visual Assets

**Pexels API**

Used to retrieve video footage for the generated content.

### Image Processing

**Pillow**

Used for thumbnail generation and image processing.

---

## ⚙️ Setup

### 1. Clone the repository

~~~bash
git clone https://github.com/Harsh-Dev19/ai-video-generation-pipeline.git
cd ai-video-generation-pipeline
~~~

### 2. Install dependencies

~~~bash
pip install -r requirements.txt
~~~

### 3. Configure environment variables

Create a `.env` file based on `.env.example`.

~~~bash
cp .env.example .env
~~~

Then add the required API credentials.

> Never commit your `.env` file or expose API keys publicly.

---

## ▶️ Run the Pipeline

Start the complete workflow with:

~~~bash
python main.py
~~~

The pipeline will execute the configured generation stages and produce the resulting assets in the output directories.

---

## 🔑 API Configuration

The pipeline relies on external APIs/services for parts of the generation process.

Typical configuration includes credentials for:

~~~text
┌─────────────────────┐
│ Google Gemini       │
├─────────────────────┤
│ Pexels              │
└─────────────────────┘
~~~

Store credentials in `.env` rather than directly inside Python source files.

---

## 📦 Output

The pipeline can produce multiple assets during the generation process, including:

- 📝 Generated script
- 🎙️ Voiceover audio
- 🎥 Video clips
- 🎬 Final video
- 🔍 SEO metadata
- 🖼️ Thumbnail

These outputs can then be used as the starting point for publishing or further editing.

---

## 🎯 Project Goal

The goal of this project is to explore how multiple AI and media-generation services can be connected into a single automated content-production workflow.

Instead of treating script generation, voice generation, visual collection, editing, SEO preparation, and thumbnail creation as separate tasks, the pipeline brings them together into one process.

---

## 📚 What This Project Explores

- Generative AI integration
- API-based automation
- Text generation
- Text-to-speech
- Video processing
- Automated media workflows
- SEO metadata generation
- Image generation and processing
- Environment-based API configuration
- Python pipeline architecture

---

## 🔮 Future Improvements

Potential improvements include:

- 🎵 Automatic background music
- 📝 Automatic subtitles
- 🎨 More advanced thumbnail generation
- 🎞️ More dynamic video transitions
- 🗣️ Multiple voice options
- 🌐 Additional content platforms
- 📊 Automated publishing
- 🧠 More advanced content planning
- ⚡ Parallelized generation stages

---

## ⚠️ Notes

The pipeline depends on external APIs and services. Availability, API limits, generated content, and service behavior may vary depending on the configured providers.

Generated media should also be reviewed before publishing.

---

## 👨‍💻 Project

**AI Video Generation Pipeline**

An automated experiment in combining generative AI, media processing, and API-driven automation into a single content creation workflow.

---

<p align="center">

<b>Built with Python • Gemini • MoviePy • Pexels • gTTS • Pillow</b>

<br><br>

⭐ If you found the project interesting, consider starring the repository.

</p>
