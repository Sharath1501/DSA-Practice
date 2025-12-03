import numpy as np
import cv2
from scipy.optimize import linear_sum_assignment
from concurrent.futures import ThreadPoolExecutor, as_completed
import torch
from ultralytics import YOLO
import time
import matplotlib.pyplot as plt

class KalmanFilter:
    def __init__(self):
        self.state = None  # Placeholder for Kalman Filter state

    def predict(self):
        # Simplified prediction step
        pass

    def update(self, detection):
        # Simplified update step
        pass

class Tracker:
    def __init__(self, id, detection):
        self.id = id
        self.kf = KalmanFilter()
        self.kf.update(detection)
        self.detection = detection

class DeepSort:
    def __init__(self):
        self.trackers = []
        self.next_id = 0

    def update(self, detections):
        # Predict new locations of existing trackers
        for tracker in self.trackers:
            tracker.kf.predict()

        # Data association step (optimized)
        if len(self.trackers) > 0 and len(detections) > 0:
            cost_matrix = np.zeros((len(self.trackers), len(detections)))
            for i, tracker in enumerate(self.trackers):
                cost_matrix[i, :] = np.linalg.norm(np.array(tracker.detection) - np.array(detections), axis=1)
            
            row_ind, col_ind = linear_sum_assignment(cost_matrix)
            
            assigned_detections = np.full(len(detections), False)
            for i, j in zip(row_ind, col_ind):
                if cost_matrix[i, j] < 50:  # Arbitrary threshold for assignment
                    tracker = self.trackers[i]
                    tracker.kf.update(detections[j])
                    tracker.detection = detections[j]
                    assigned_detections[j] = True

            # Manage lost trackers and create new trackers
            new_trackers = []
            for i, assigned in enumerate(assigned_detections):
                if not assigned:
                    new_trackers.append(Tracker(self.next_id, detections[i]))
                    self.next_id += 1
            self.trackers.extend(new_trackers)
        else:
            # If there are no existing trackers or no detections, create new trackers
            for detection in detections:
                self.trackers.append(Tracker(self.next_id, detection))
                self.next_id += 1

def process_frame(model, frame):
    results = model(frame)
    detections = []
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
            w, h = x2 - x1, y2 - y1
            detections.append(np.array([x1, y1, w, h]))
    return detections

def run_deepsort_on_video(video_path, skip_interval=5):
    cap = cv2.VideoCapture(video_path)
    deepsort = DeepSort()
    model = YOLO('yolov8s.pt')  # Load YOLOv8 model

    frame_times = []
    cumulative_time = 0
    frame_count = 0

    start_time = time.time()

    with ThreadPoolExecutor(max_workers=2) as executor:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            if frame_count % (skip_interval + 1) == skip_interval:
                frame_count += 1
                continue

            start_frame_time = time.time()
            results = model(frame)
            detections = []
            for result in results:
                for box in result.boxes:
                    x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                    w, h = x2 - x1, y2 - y1
                    detections.append(np.array([x1, y1, w, h]))

            deepsort.update(detections)
            frame_count += 1

            end_frame_time = time.time()
            processing_time = end_frame_time - start_frame_time
            frame_times.append(processing_time)
            cumulative_time += processing_time

            # Display results
            for tracker in deepsort.trackers:
                x, y, w, h = tracker.detection
                cv2.rectangle(frame, (int(x), int(y)), (int(x+w), int(y+h)), (255, 0, 0), 2)
                cv2.putText(frame, f'ID: {tracker.id}', (int(x), int(y-10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            cv2.imshow('Deep SORT', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

    end_time = time.time()
    total_time = end_time - start_time

    # Print total time taken
    print(f"Total processing time: {total_time:.2f} seconds")

    # Plotting frame processing time distribution
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.plot(frame_times)
    plt.xlabel('Frame Index')
    plt.ylabel('Frame Processing Time (seconds)')
    plt.title('Frame Processing Time Distribution')

    plt.subplot(2, 1, 2)
    plt.plot(np.cumsum(frame_times))
    plt.xlabel('Frame Index')
    plt.ylabel('Cumulative Time (seconds)')
    plt.title('Cumulative Processing Time')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    video_path = 'l.mp4'
    run_deepsort_on_video(video_path, skip_interval=5)
