from youtube_transcript_api import YouTubeTranscriptApi
from sign_language_production import text_to_pose_and_gif


def subtitle(video_id):
    """
    This function retrieves full subtitle in a YouTube video.
    :param video_id: id of YouTube video
    :return: 1 string of the subtitle (full)
    """
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    output = ''
    for x in transcript:
        sentence = x['text']
        output += f' {sentence}'

    return output


def create_gif(subtitle_string: str, gif_dir: str, url: str):
    """
    This function creates a GIF file from a subtitle string.
    :param url: url of the YouTube video passed in - used as filename later
    :param gif_dir: directory to save the GIF file
    :param subtitle_string: string of the subtitle
    :return: None
    """

    # time_now = time.strftime("%Y%m%d-%H%M%S")
    text_to_pose_and_gif(
        text_input=subtitle_string,
        pose_filename=f"{url}.pose",
        pose_dir="assets/pose",
        gif_dir=gif_dir,
        target_language="de",
        translator_machine="google",
        glosser="simple",
        lexicon_dataset="signsuisse",
        signed_language="dsgs"
    )
