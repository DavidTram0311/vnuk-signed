# VNUK-SIGNED WEBSITE
python 3.8.19

Install packages

```
pip install -r requirements.txt
```

# How to run

```commandline
python app.py
```

# Project Structure
```commandline
.
├── app.py
├── templates
│   ├── index.html
│   ├── input_form.html
│   └── translated.html
├── static
│   └── images
│       └── gif
├── assets
│   └── pose
│       └── your_pose_file.pose
└── README.md

```

# Application Workflow
### 1. Home Page (/)
Route: ```/```

Method: ```GET```

Template: index.html

Description: The home page presents a simple interface for users to navigate to the input form.
### 2. Input Form (/input_form)
Route: ```/input_form```

Methods: ``GET``, ``POST``

Template: input_form.html

Description:

GET: Displays the form for users to input the YouTube video URL.

POST: Handles the submitted form data.

Extracts the video ID from the URL.

Clears any existing GIFs in the static/images/gif directory.
Reads the pose data file.

Uses ``PoseVisualizer`` to create and save an animated GIF of the pose.
Redirects to the translated page with the video URL.

### 3. Translated Page (/translated/<url>)
Route: ```/translated/<url>```

Method: ``GET``

Template: translated.html

Description: Displays the results, including the generated GIF and the extracted subtitles.
### 4. Subtitle Extraction Function (subtitle(video_id))
Function: ```subtitle(video_id)```

Description: Retrieves the full subtitle text from a YouTube video using the YouTubeTranscriptApi.


