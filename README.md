# Deaf YouTube support tool: Sign Language Pose Producer for YouTube Videos  
This tool creates sign language representation (poses) for a YouTube Video. Users (especially the Deaf Community) can watch and understand the YouTube video with this poses representation of video's content.

To use this tool, the YouTube video must have transcript.  

**Note:** It might take a (long) while to create the representation for your "first-time" video. We are working to improve this.

## Web App - Installation 
1. Clone this repository to your local machine.

2. Install the required packages     
(Checkout the `dev_notes.md` for more details on the installation process in case you encounter any issues.)  
Running the following command in terminal:
```commandline
pip install -r requirements.txt
```


3. Prepare the lexicon dataset (for Swiss-German Sign Language):  
- Download the [signsuisse lexicon dataset]([https://drive.usercontent.google.com/download?id=1sVEASYo7CRQ1xfaXgPO8Mg1r4Hpux-vh&export=download](https://drive.google.com/file/d/1sVEASYo7CRQ1xfaXgPO8Mg1r4Hpux-vh/view?usp=sharing))
- Extract the downloaded files to the directory `vnuk-signed/sign_language_production/gloss_to_pose/datasets/signsuisse`
- The directory `signsuisse` data folder should contain:
  - `index.csv`
  - `de_dsgs_poses` (includes .pose files for each word/gloss)
4. Run the web app:
- Manually run "app.py", or
- Run the following command in terminal under the directory `vnuk-signed`:
```commandline
python app.py
```  
Input one of the following YouTube video URLs to use the prepared demo for faster use:
> https://www.youtube.com/watch?v=MkWta2k0k_g  
https://www.youtube.com/watch?v=m62fZr0CTqE  
https://www.youtube.com/watch?v=oqoSKW1WWZc  
https://www.youtube.com/watch?v=V1ah6tmNUz8  
https://www.youtube.com/watch?v=SUt8q0EKbms  
https://www.youtube.com/watch?v=i4YoxY9ydwQ  

## CLI pipeline: from text to sign language poses
#### If you are interested in converting any text to sign language poses, you can use this CLI pipeline to manually input the text.
To run this pipeline (CLI version) in terminal, first move the terminal to under directory `vnuk-signed/sign_language_production`.  
For example, to convert the sentence below from English spoken text to Swiss-German Sign Language pose:  
```commandline
python main_CLI.py --text_input "Good morning, we have planned a picnic in the garden." --pose_filename "{your_filename}.pose" --target_language "de" --translator_machine "google" --glosser "simple" --lexicon_dataset "signsuisse" --signed_language "dsgs" 
```

## (For development) Call the pipeline module
#### If you want to you this pipeline in developing a new feature, you can call the pipeline module in your python script.
For example, a python .py file in `vnuk-signed` directory can call the pipeline module as follows:
```python
from sign_language_production import text_to_pose_and_gif

# Prepare the input parameters before calling the pipeline function
text_to_pose_and_gif(
    text_input="Good morning, we have planned a picnic in the garden.",
    pose_filename="xxx.pose",
    pose_dir="assets/pose",
    gif_dir="assets/gif",
    target_language="de",
    translator_machine="google",
    glosser="simple",
    lexicon_dataset="signsuisse",
    signed_language="dsgs"
)
```
