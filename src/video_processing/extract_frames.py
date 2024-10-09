import cv2
import os

def extract_frames(video_path, output_folder, frame_rate=1):
    """
    Extracts frames from a video file at a specified frame rate.
    
    Args:
        video_path (str): Path to the input video file.
        output_folder (str): Directory where extracted frames will be saved.
        frame_rate (int): Number of frames to extract per second.

    Returns:
        int: Number of frames extracted.
    """
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Capture the video
    video_capture = cv2.VideoCapture(video_path)
    
    # Frame counter
    frame_count = 0
    extracted_frame_count = 0

    # Read until the end of the video
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        
        # Save the frame at the specified frame rate
        if frame_count % frame_rate == 0:
            frame_filename = os.path.join(output_folder, f"frame_{extracted_frame_count}.jpg")
            cv2.imwrite(frame_filename, frame)
            extracted_frame_count += 1

        frame_count += 1

    video_capture.release()
    return extracted_frame_count

if __name__ == "__main__":
    video_path = "path/to/your/video.mp4"  # Specify your video file path
    output_folder = "output_frames"         # Specify the output directory for frames
    frames_extracted = extract_frames(video_path, output_folder, frame_rate=30)
    print(f"Extracted {frames_extracted} frames from the video.")
