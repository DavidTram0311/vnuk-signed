# Prepare the dataset for generating poses

## SignSuisse dataset
- For a full data preparation process, follow the Colab notebook `signsuisse_proprocessing.ipynb`.
- If you already have the signsuisse dataset downloaded and unzipped locally, simply run `signsuisse_move_files.py`.

### Changes:
The dataset from SwissUbase includes: openpose and mediapipe pose data.  
The gloss_to_pose module uses mediapipe data structure run the script to prepare index and .pose folder for `example_mediapipe`