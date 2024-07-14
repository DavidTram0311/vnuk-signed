from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound
from sign_language_production import text_to_pose_and_gif


def subtitle(video_id):
    """
    This function retrieves full subtitle in a YouTube video.
    :param video_id: id of YouTube video
    :return: 1 string of the subtitle (full)
    """
    langs = [
        'af', 'ak', 'sq', 'am', 'ar', 'hy', 'as', 'ay', 'az', 'bn', 'eu', 'be', 'bho', 'bs', 'bg', 'my', 'ca',
        'ceb', 'zh-Hans', 'zh-Hant', 'co', 'hr', 'cs', 'da', 'dv', 'nl', 'en', 'eo', 'et', 'ee', 'fil', 'fi',
        'fr', 'gl', 'lg', 'ka', 'de', 'el', 'gn', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig',
        'id', 'ga', 'it', 'ja', 'jv', 'kn', 'kk', 'km', 'rw', 'ko', 'kri', 'ku', 'ky', 'lo', 'la', 'lv', 'ln',
        'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'ne', 'nso', 'no', 'ny', 'or', 'om', 'ps',
        'fa', 'pl', 'pt', 'pa', 'qu', 'ro', 'ru', 'sm', 'sa', 'gd', 'sr', 'sn', 'sd', 'si', 'sk', 'sl', 'so',
        'st', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'tt', 'te', 'th', 'ti', 'ts', 'tr', 'tk', 'uk', 'ur', 'ug',
        'uz', 'vi', 'cy', 'fy', 'xh', 'yi', 'yo', 'zu'
    ]
    # transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=langs)
    # output = ''
    # for x in transcript:
    #     sentence = x['text']
    #     output += f' {sentence}'
    # return output
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=langs)
        return True, transcript
    except NoTranscriptFound:
        return False, "No transcript available for this video."
    except Exception as e:
        return False, f"An error occurred: {str(e)}"

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
