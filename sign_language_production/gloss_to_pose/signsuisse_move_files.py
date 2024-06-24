import pandas as pd
import os
import shutil

df = pd.read_csv("datasets/signsuisse/index.csv")

# Get the "id" column as a list
id_list = df["id"].tolist()

# Check if the "de_dsgs_poses" folder exists, if not create it
if not os.path.exists("datasets/signsuisse/de_dsgs_poses"):
    os.makedirs("datasets/signsuisse/de_dsgs_poses")

# path to "openpose.v1.0/openpose" folder
# openpose_folder_path = "E:\projects\graduation\spoken2signed\spoken-to-signed-translation\\assets\signsuisse\openpose"

# path to "example_mediapipe" folder
openpose_folder_path = "E:\projects\graduation\spoken2signed\spoken-to-signed-translation\\assets\signsuisse\example_mediapipe"

destination = "datasets/signsuisse/de_dsgs_poses"

# Iterate over the id_list and get the corresponding .pose files
for pose_id in id_list:
    file_name = str(pose_id) + ".pose"
    print(file_name)
    pose_file_path = os.path.join(openpose_folder_path, file_name)
    pose_destination_path = os.path.join(destination, file_name)
    print(pose_file_path)
    if os.path.exists(pose_file_path):
        # Copy the .pose file to the "de_dsgs_poses" folder
        print("Copying {} to de_dsgs_poses".format(file_name))
        # !cp {pose_file_path} de_dsgs_poses
        shutil.copy(pose_file_path, pose_destination_path)
    else:
        print("Fail to copy file {} to {}".format(pose_file_path, destination))
