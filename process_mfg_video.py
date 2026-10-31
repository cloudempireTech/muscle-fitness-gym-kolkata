import os
import shutil
import subprocess

src_video = r"C:\Users\dasan\.gemini\antigravity\scratch\premium-fitness-studio-kolkata\assets\videos\hero.mp4"
dest_video = r"C:\Users\dasan\.gemini\antigravity\scratch\muscle-fitness-gym-kolkata\assets\videos\hero.mp4"
dest_poster = r"C:\Users\dasan\.gemini\antigravity\scratch\muscle-fitness-gym-kolkata\assets\images\hero-poster.jpg"

print(f"Copying 16:9 fitness video from {src_video}...")
shutil.copyfile(src_video, dest_video)
print(f"Copied hero.mp4 ({os.path.getsize(dest_video)} bytes)")

# Extract poster at 1.5s
print("Extracting poster at 1.5s...")
subprocess.run([
    "ffmpeg", "-y", "-i", dest_video,
    "-ss", "00:00:01.500",
    "-vframes", "1",
    "-q:v", "2",
    dest_poster
], check=True)
print(f"Poster extracted: {dest_poster} ({os.path.getsize(dest_poster)} bytes)")

# Ensure +faststart
temp_fast = r"C:\Users\dasan\.gemini\antigravity\scratch\muscle-fitness-gym-kolkata\assets\videos\hero_fast.mp4"
print("Optimizing video with +faststart...")
subprocess.run([
    "ffmpeg", "-y", "-i", dest_video,
    "-c:v", "copy",
    "-c:a", "copy",
    "-movflags", "+faststart",
    temp_fast
], check=True)

if os.path.exists(temp_fast) and os.path.getsize(temp_fast) > 50000:
    shutil.copyfile(temp_fast, dest_video)
    os.remove(temp_fast)
    print(f"Verified hero.mp4 with +faststart ({os.path.getsize(dest_video)} bytes)")

print("VIDEO SETUP COMPLETE FOR MUSCLE FITNESS GYM 2!")
