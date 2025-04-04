import cv2
import os

# Define video and output folder
video_path = 'video_data.mp4'  # Video is in the same folder as the script
output_dir = 'frames'  # Folder to save extracted frames

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Open video file
cap = cv2.VideoCapture(video_path)
i = 0
frame_skip = 6
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if i > frame_skip - 1:
        frame_count += 1
        frame_filename = os.path.join(output_dir, f'frame{frame_count}.jpg')
        cv2.imwrite(frame_filename, frame)
        i = 0
        continue

    i += 1

cap.release()
cv2.destroyAllWindows()
