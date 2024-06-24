# Gloss-to-Pose

Receive a list of glosses from previous steps and return a sequence of poses.

```python
gloss_to_pose.gloss_to_pose(gloss, lexicon_directory, spoken_language="", signed_language="")
```

The `lexicon_directory` is the path to the directory containing the lexicon files.  
It should contain a index.csv file with the following structure:

```csv
path,spoken_language,signed_language,start,end,words,glosses,priority
```
  and a folder `folder_name` containing the .pose files.
  