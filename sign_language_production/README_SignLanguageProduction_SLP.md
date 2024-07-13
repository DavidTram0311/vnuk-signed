This pipeline serves the purpose of converting spoken text to sign language pose (MediaPipe OpenPose - 2D skeleton).  
More details of the project:  
1. Translate spoken text in any language to German/Swiss-German.
2. Text to Gloss: spoken German/Swiss-German text to corresponding gloss of Swiss-German Sign Language.
3. Gloss to Pose: Swiss-German Sign Language gloss to corresponding pose (OpenPose - 2D skeleton).

(Major) Pipeline components:  
- py-trans
- text-to-gloss module
- Pose lookup (to map gloss to pose) and smoothing (concatenate + smoothen)

Usage from terminal in `sign-language-production` directory:  
For example, to convert the sentence below from English spoken text to Swiss-German Sign Language pose:  
```commandline
python main_CLI.py --text_input "Good morning, we have planned a picnic in the garden." --pose_filename "{your_filename}.pose" --target_language "de" --translator_machine "google" --glosser "simple" --lexicon_dataset "signsuisse" --signed_language "dsgs" 
```
