# Deaf YouTube support tool: Sign Language Producer for YouTube Videos

## CLI pipeline: from text to sign language poses
To run this pipeline (CLI version) in terminal, first move the terminal to under directory `vnuk-signed/sign_language_production`.  
For example, to convert the sentence below from English spoken text to Swiss-German Sign Language pose:  
```
python main.py --text_input "Good morning, we have planned a picnic in the garden." --pose_filename "xxx.pose"--target_language "de" --translator_machine "google" --glosser "simple" --lexicon_dataset "signsuisse" --signed_language "dsgs" 

```

## (For development) Call the pipeline module
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

## GUI pipeline: (to be updated)
(internal dev notes) In terminal, branch main  
```commandline
git checkout update-webapp-response
```
#### Update tasks - Priority order:
1. Loading sign: inform user to wait for GIF generation
2. Auto-play YouTube video whenever reloading page
3. GIF at the center of its container
