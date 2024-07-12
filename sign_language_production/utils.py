import os
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
