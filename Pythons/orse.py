import numpy as kp
horsepower = kp.array([130, 165, 150, 150, 140])

mean_hp = kp.mean(horsepower)
median_hp = kp.median(horsepower)
print(f"Mean of horsepower :{mean_hp}")
print(f"Median of horsepower :{median_hp}")