from moviepy import VideoFileClip, AudioFileClip, concatenate_videoclips

TARGET_WIDTH = 1280
TARGET_HEIGHT = 720

def resize_clip(clip):
    # Resize while keeping aspect ratio
    clip = clip.resized(height=TARGET_HEIGHT)

    # Crop center if width is larger than target
    if clip.w > TARGET_WIDTH:
        x_center = clip.w // 2
        clip = clip.cropped(
            x_center - TARGET_WIDTH // 2,
            0,
            x_center + TARGET_WIDTH // 2,
            TARGET_HEIGHT
        )

    return clip


def create_video(video_paths, audio_path):
    clips = []

    for path in video_paths:
        clip = VideoFileClip(path)
        clip = resize_clip(clip)
        clips.append(clip)

    video = concatenate_videoclips(clips, method="compose")

    audio = AudioFileClip(audio_path)

    video = video.with_duration(audio.duration)
    final = video.with_audio(audio)

    final.write_videofile("final_output.mp4", fps=24)
