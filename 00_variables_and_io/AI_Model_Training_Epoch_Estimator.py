"""
Task:
Estimate the total time required to train a Large Language Model (LLM) on a GPU cluster.

Input Format:
Line 1 (int): Total number of epochs (complete passes through the dataset).       
Line 2 (int): Total dataset size in Gigabytes (GB).
Line 3 (float): GPU cluster processing speed (GB per hour).

Output Format:
Print the total training time in hours and days.
"""
#Solution
epoch = int(input("Total Epochs: "))
dataset_size = int(input("Total Dataset Size(GB): "))
processing_speed = float(input("Enter GPU Cluster Processing Speed(GB per hour): "))
total_hours = epoch * dataset_size / processing_speed
total_days = total_hours / 24

print(f"Total Training Time: {total_hours:.2f} hours or {total_days:.2f} days")