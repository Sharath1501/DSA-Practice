import numpy as np
import cv2
from scipy.optimize import linear_sum_assignment
from joblib import Parallel, delayed
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
    def __init__(self, optimized=False):
        self.trackers = []
        self.next_id = 0
        self.optimized = optimized
        if optimized:
            self.n_jobs = -1  # Use all available CPU cores
        else:
            self.n_jobs = 1  # Use single core for original version

    def update(self, detections):
        if self.optimized:
            Parallel(n_jobs=self.n_jobs)(delayed(self._predict)(tracker) for tracker in self.trackers)
        else:
            for tracker in self.trackers:
                tracker.kf.predict()

        assigned_detections = [False] * len(detections)
        cost_matrix = np.zeros((len(self.trackers), len(detections)))
        for i, tracker in enumerate(self.trackers):
            for j, detection in enumerate(detections):
                cost_matrix[i, j] = np.linalg.norm(tracker.detection - detection)
        
        row_ind, col_ind = linear_sum_assignment(cost_matrix)

        if self.optimized:
            Parallel(n_jobs=self.n_jobs)(delayed(self._update_tracker)(self.trackers[i], detections[j], assigned_detections, j) for i, j in zip(row_ind, col_ind) if cost_matrix[i, j] < 50)
        else:
            for i, j in zip(row_ind, col_ind):
                if cost_matrix[i, j] < 50:
                    tracker = self.trackers[i]
                    tracker.kf.update(detections[j])
                    tracker.detection = detections[j]
                    assigned_detections[j] = True

        new_trackers = [Tracker(self.next_id, detections[i]) for i, assigned in enumerate(assigned_detections) if not assigned]
        self.next_id += len(new_trackers)
        self.trackers.extend(new_trackers)

    def _predict(self, tracker):
        tracker.kf.predict()

    def _update_tracker(self, tracker, detection, assigned_detections, detection_index):
        tracker.kf.update(detection)
        tracker.detection = detection
        assigned_detections[detection_index] = True

def run_deepsort_on_video(video_path, optimized=False):
    cap = cv2.VideoCapture(video_path)
    deepsort = DeepSort(optimized)
    model = YOLO('yolov8s.pt')  # Load YOLOv8 model

    start_time = time.time()
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        results = model(frame)
        detections = []
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = box.xyxy.numpy()[0]
                w, h = x2 - x1, y2 - y1
                detections.append(np.array([x1, y1, w, h]))

        deepsort.update(detections)

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
    
    return end_time - start_time

if __name__ == "__main__":
    video_path = 'l.mp4'
    
    original_time = run_deepsort_on_video(video_path, optimized=False)
    optimized_time = run_deepsort_on_video(video_path, optimized=True)
    
    print(f"Original Deep SORT Time: {original_time:.6f} seconds")
    print(f"Optimized Deep SORT Time: {optimized_time:.6f} seconds")

    # Plotting the results
    labels = ['Original', 'Optimized']
    times = [original_time, optimized_time]

    plt.bar(labels, times, color=['blue', 'green'])
    plt.ylabel('Execution Time (seconds)')
    plt.title('Deep SORT Execution Time Comparison')
    plt.show()
