from pose_format import Pose
from .concatenate import concatenate_poses
from .lookup import CSVPoseLookup
from ..text_to_gloss.custom_types import Gloss


def gloss_to_pose(glosses: Gloss,
                  lexicon_directory: str,
                  spoken_language: str,
                  signed_language: str) -> Pose:
    """
    This function takes a list of glosses and returns a single Pose object
    that represents the sequence of poses for input glosses.
    :param glosses: list of glosses in Gloss type
    :param lexicon_directory: lexicon directory contains index.csv and folder of .pose files
    :param spoken_language:
    :param signed_language:
    :return: a single Pose object that represents the input sequence of poses
    """
    # TODO: double check os directory for the lexicon directory
    pose_lookup = CSVPoseLookup(lexicon_directory)
    # Transform the list of glosses into a list of poses
    poses = pose_lookup.lookup_sequence(glosses, spoken_language, signed_language)

    # Concatenate the poses to create a single pose
    return concatenate_poses(poses)
