import os
from collections import defaultdict
from typing import List
from pose_format import Pose
from ...text_to_gloss.types import Gloss


def make_dictionary_index(rows: List, based_on: str):
    """
    Store index in a dictionary for faster lookup/retrieve.
    Only store path to the .pose file.
    :param rows: a row of index.csv file includes: path,spoken_language,signed_language,start,end,words,glosses,priority
    :param based_on: create the index based on either "words" or "glosses" column
    :return: Dictionary index: {spoken_language: {signed_language: {term: [path]}}}
    """
    languages_dict = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for d in rows:
        lower_term = d[based_on].lower()
        languages_dict[d['spoken_language']][d['signed_language']][lower_term].append({
            "path": d['path']
        })
    return languages_dict


class PoseLookup:
    """
    Base class for looking up poses based on glosses
    """
    def __init__(self, rows: List, lexicon_directory: str = None):
        self.directory = lexicon_directory
        self.words_index = make_dictionary_index(rows, based_on="words")
        self.glosses_index = make_dictionary_index(rows, based_on="glosses")

    def read_pose(self, pose_path: str):
        if self.lexicon_directory is None:
            raise ValueError("Can't access pose files without specifying a directory")

        # TODO: double check os directory for the lexicon directory
        pose_path = os.path.join(self.lexicon_directory, pose_path)
        with open(pose_path, "rb") as f:
            return Pose.read(f.read())

    def lookup(self, word: str, gloss: str, spoken_language: str, signed_language: str) -> Pose:
        """
        Look up a pose based on word and gloss
        """
        # Create a list of possible lookups
        # Order of lookup: words_index by word -> glosses_index by word -> glosses_index by gloss
        # This order make better sense, as the word is the most specific term, and gloss is the most general term
        # Also word is more stable; and is more likely to be unique than gloss
        lookup_list = [
            (self.words_index, (spoken_language, signed_language, word)),
            (self.glosses_index, (spoken_language, signed_language, word)),
            (self.glosses_index, (spoken_language, signed_language, gloss)),
        ]

        for dict_index, (spoken_language, signed_language, term) in lookup_list:
            if spoken_language in dict_index:
                if signed_language in dict_index[spoken_language]:
                    lower_term = term.lower()
                    if lower_term in dict_index[spoken_language][signed_language]:
                        rows = dict_index[spoken_language][signed_language][lower_term]
                        return self.read_pose(rows[0]["path"])

        raise FileNotFoundError

    def lookup_sequence(self, glosses: Gloss, spoken_language: str, signed_language: str):
        """
        Look up a sequence of poses based on a sequence of glosses (words and glosses)
        """
        poses: List[Pose] = []
        for word, gloss in glosses:
            try:
                pose = self.lookup(word, gloss, spoken_language, signed_language)
                poses.append(pose)
            except FileNotFoundError:
                pass

        gloss_sequence = ' '.join([f"{word}/{gloss}" for word, gloss in glosses])
        if len(poses) == 0:
            raise Exception(f"No poses found for {gloss_sequence}")

        print(f"Pose created complete for {gloss_sequence}")
        return poses
