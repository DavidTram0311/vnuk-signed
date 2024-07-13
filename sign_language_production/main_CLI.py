import argparse
from text_to_gloss import text2gloss_module
from gloss_to_pose import gloss_to_pose
from text_translate import translate_text
import os
from utils import resize_and_generate_gif
from utils import download_dataset


def translate_text_input(text_input, target_language, translator_machine):
    """Translate the input text to the target language using the specified translator."""
    translation_result = translate_text(text=text_input, target_language=target_language,
                                        translator_machine=translator_machine)
    return translation_result['translation']


def convert_text_to_gloss(text_translated, target_language, glosser):
    """Convert translated text to gloss."""
    text2gloss = text2gloss_module(glosser=glosser)
    glosses = text2gloss(text=text_translated, language=target_language)
    return glosses


def convert_gloss_to_pose(glosses, lexicon_dataset, target_language, signed_language):
    """Convert gloss to pose sequence."""
    poses_sequence = gloss_to_pose(glosses=glosses, lexicon_dataset=lexicon_dataset, spoken_language=target_language,
                                   signed_language=signed_language)
    return poses_sequence


def save_pose_sequence(poses_sequence, pose_filename):
    """Save the pose sequence to a .pose file."""
    with open(pose_filename, "wb") as f:
        poses_sequence.write(f)


def main(args):
    """Main function to execute the translation, glossing, pose generation, and visualization process."""
    print("Starting the process...")

    # Step 1: Translate text
    text_translated = translate_text_input(args.text_input, args.target_language, args.translator_machine)
    print("Checkpoint 1 - text translation: DONE")

    # Step 2: Convert text to gloss
    glosses = convert_text_to_gloss(text_translated, args.target_language, args.glosser)
    print("Checkpoint 2 - text to gloss: DONE")

    # Step 3: Convert gloss to pose sequence
    # download_dataset(dataset_name=args.lexicon_dataset)
    poses_sequence = convert_gloss_to_pose(glosses, args.lexicon_dataset, args.target_language, args.signed_language)

    # Save poses sequence to a .pose file
    save_pose_sequence(poses_sequence, args.pose_filename)
    print("Checkpoint 3 - text to poses sequence: DONE")

    # Step 4: Resize poses for visualization and generate .gif
    # Derive gif file name from pose sequence file
    gif_name = os.path.splitext(args.pose_filename)[0] + ".gif"
    resize_and_generate_gif(poses_sequence, gif_name)
    print("Checkpoint 4 - pose to gif: DONE")

    print("Final checkpoint: text-trans-text-gloss-pose-gif DONE")


if __name__ == "__main__":
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Convert text to pose sequence and generate a visualization GIF.")
    parser.add_argument("--text_input", type=str, required=True, help="The input text to be translated.")
    parser.add_argument("--target_language", type=str, default="de",
                        help="The target language for translation (default: 'de').")
    parser.add_argument("--translator_machine", type=str, default="google",
                        help="The translator machine to use (default: 'google').")
    parser.add_argument("--glosser", type=str, default="simple",
                        help="The glosser to use for text to gloss conversion (default: 'simple').")
    parser.add_argument("--lexicon_dataset", type=str, default="signsuisse",
                        help="The lexicon dataset to use for gloss to pose conversion (default: 'signsuisse').")
    parser.add_argument("--signed_language", type=str, default="dsgs",
                        help="The signed language to use (default: 'dsgs').")
    parser.add_argument("--pose_filename", type=str, required=True,
                        help="The file name to save the pose sequence (must have .pose extension).")

    args = parser.parse_args()
    main(args)
