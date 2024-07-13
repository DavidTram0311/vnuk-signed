import os
import urllib.request
import zipfile
from pose_format.pose_visualizer import PoseVisualizer


def resize_and_generate_gif(poses_sequence, gif_name, gif_dir="."):
    """
    Resize pose sequence for visualization and generate a GIF.

    Args:
        poses_sequence (Pose): The pose sequence to be resized and visualized.
        gif_name (str): The name of the .gif file.
        gif_dir (str): Directory to save the .gif file.

    Returns:
        None
    """
    print("Resizing poses for visualization...")
    # Resize to 256, for visualization speed
    scale = poses_sequence.header.dimensions.width / 256
    poses_sequence.header.dimensions.width = int(poses_sequence.header.dimensions.width / scale)
    poses_sequence.header.dimensions.height = int(poses_sequence.header.dimensions.height / scale)
    poses_sequence.body.data = poses_sequence.body.data / scale

    # Ensure gif_dir exists
    if not os.path.exists(gif_dir):
        os.makedirs(gif_dir)

    # Derive gif file name
    print("Generating GIF from poses sequence...")
    gif_file_path = os.path.join(gif_dir, gif_name)
    v = PoseVisualizer(poses_sequence)
    print("GIF created, saving...")
    v.save_gif(gif_file_path, v.draw())
    print("GIF saved at:", gif_file_path)


# TODO: Prepare/Download the dataset function
def download_dataset(dataset_name, dataset_dir="gloss_to_pose/datasets"):
    """
    Downloads a dataset zip file from a given URL and saves it to the specified directory.
    :param dataset_dir:
    :param dataset_name:
    :return:
    """
    urls_dict = {
        "signsuisse": "https://drive.usercontent.google.com/download?id=1sVEASYo7CRQ1xfaXgPO8Mg1r4Hpux-vh&export=download",
        "vietsign": ""
    }

    dataset_path = os.path.join(dataset_dir, dataset_name)
    # Check if the dataset is ready
    if os.path.exists(dataset_path):
        print(f"Dataset {dataset_name} is already downloaded.")
        return

    print("Dataset {} not found. It might take a while to prepare the dataset.".format(dataset_name))
    # Ensure the directory exists
    os.makedirs(dataset_dir, exist_ok=True)
    dataset_url = urls_dict[dataset_name]
    dataset_zippath = os.path.join(dataset_dir, f"{dataset_name}.zip")
    # Download the dataset ZIP file
    print('Downloading {} dataset...'.format(dataset_name))
    urllib.request.urlretrieve(dataset_url, dataset_zippath)
    print('Dataset {} downloaded. Now unzipping...'.format(dataset_name))
    # Unzip the dataset
    with zipfile.ZipFile(dataset_zippath, 'r') as zip_ref:
        zip_ref.extractall(os.path.join(dataset_path))
    print('Dataset {} unzipped.'.format(dataset_name))
