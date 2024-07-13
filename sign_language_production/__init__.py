import os
from text_to_gloss import text2gloss_module
from gloss_to_pose import gloss_to_pose
from text_translate import translate_text
from .utils import resize_and_generate_gif
from .utils import download_dataset


def text_to_pose_and_gif(text_input, pose_filename, pose_dir, gif_dir, target_language="de", translator_machine="google",
                         glosser="simple", lexicon_dataset="signsuisse", signed_language="dsgs"):
    """
    Convert input text to a pose sequence and generate a visualization GIF.

    Args:
        text_input (str): The input text to be translated.
        pose_filename (str): The name of the .pose file.
        pose_dir (str): Directory to save the .pose file.
        gif_dir (str): Directory to save the .gif file.
        target_language (str, optional): The target language for translation. Defaults to "de".
        translator_machine (str, optional): The translator machine to use. Defaults to "google".
        glosser (str, optional): The glosser to use for text to gloss conversion. Defaults to "simple".
        lexicon_dataset (str, optional): The lexicon dataset to use for gloss to pose conversion. Defaults to "signsuisse".
        signed_language (str, optional): The signed language to use. Defaults to "dsgs".

    Returns:
        None
    """
    print("Starting the process...")

    # Step 1: Translate text
    translation_result = translate_text(text=text_input, target_language=target_language,
                                        translator_machine=translator_machine)
    text_translated = translation_result['translation']
    print("Checkpoint 1 - text translation: DONE")

    # Step 2: Convert text to gloss
    text2gloss = text2gloss_module(glosser=glosser)
    glosses = text2gloss(text=text_translated, language=target_language)
    print("Checkpoint 2 - text to gloss: DONE")

    # Step 3: Convert gloss to pose sequence
    # TODO: Check if lexicon_dataset is available, if not download and place it in the correct directory
    # download_dataset(dataset_name=lexicon_dataset)
    poses_sequence = gloss_to_pose(glosses=glosses, lexicon_dataset=lexicon_dataset, spoken_language=target_language,
                                   signed_language=signed_language)

    # Ensure pose_dir exists
    if not os.path.exists(pose_dir):
        os.makedirs(pose_dir)

    # Save poses sequence to a .pose file
    pose_file_path = os.path.join(pose_dir, pose_filename)
    with open(pose_file_path, "wb") as f:
        poses_sequence.write(f)
    print("Checkpoint 3 - text to poses sequence: DONE")

    # Step 4: Resize poses for visualization and generate .gif
    # Derive gif file name from pose sequence file
    gif_name = os.path.splitext(pose_filename)[0] + ".gif"
    resize_and_generate_gif(poses_sequence, gif_name, gif_dir)
    print("Checkpoint 4 - pose to gif: DONE")

    print("Final checkpoint: text-trans-text-gloss-pose-gif DONE")
