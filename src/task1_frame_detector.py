import cv2
import os
import sys
import shutil


def extract_frames(video_source, output_dir="outputs/extracted_frames", target_fps=2):
    """
    Extract frames from video at fixed FPS.

    Parameters:
    - video_source: file path OR 0 for webcam
    - output_dir: folder to save frames
    - target_fps: number of frames per second to extract
    """

    # 🔥 Clear old extracted frames (important!)
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_source)

    if not cap.isOpened():
        print("❌ Error: Unable to open video source.")
        return

    original_fps = cap.get(cv2.CAP_PROP_FPS)

    if original_fps == 0:
        original_fps = 30  # fallback if FPS not detected

    frame_interval = int(original_fps / target_fps)

    print(f"📹 Processing video: {video_source}")
    print(f"Original FPS: {original_fps}")
    print(f"Extracting {target_fps} frames per second...")
    print(f"Frame interval: {frame_interval}")

    frame_count = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Save only selected frames
        if frame_count % frame_interval == 0:
            filename = os.path.join(output_dir, f"frame_{saved_count:05d}.jpg")
            cv2.imwrite(filename, frame)
            saved_count += 1

        frame_count += 1

    cap.release()

    print(f"✅ Done. Total frames saved: {saved_count}")


if __name__ == "__main__":

    # 🔥 Get video path from Flask (command-line argument)
    if len(sys.argv) < 2:
        print("❌ No video path provided.")
        sys.exit(1)

    video_path = sys.argv[1]

    extract_frames(
        video_source=video_path,
        target_fps=2
    )
