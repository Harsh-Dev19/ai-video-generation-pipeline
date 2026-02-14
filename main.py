from generators.script_generator import generate_script
from generators.voice_generator import generate_voice
from generators.seo_generator import generate_seo
from generators.thumbnail_generator import create_thumbnail

from media.media_fetcher import fetch_videos
from media.video_generator import create_video


def main():
    topic = input("Enter video topic: ")

    print("Generating script...")
    script = generate_script(topic)

    print("Generating voice...")
    audio_path = generate_voice(script)

    print("Fetching video...")
    video_paths = fetch_videos(topic)

    if not video_paths:
        print("Video fetch failed.")
        return

    print("Creating final video...")
    create_video(video_paths, audio_path)

    print("Generating SEO metadata...")
    seo_content = generate_seo(script)

    with open("video_metadata.txt", "w", encoding="utf-8") as f:
        f.write(seo_content)

    print("Generating thumbnail...")
    # Extract title from SEO output
    title_line = seo_content.split("TITLE:")[1].split("\n")[1].strip()
    create_thumbnail(title_line)

    print("✅ All Done! Video, metadata & thumbnail created.")


if __name__ == "__main__":
    main()
