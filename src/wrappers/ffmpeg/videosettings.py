from fractions import Fraction

from wrappers.ffmpeg.ffprobe import get_video_info, get_width_height, get_frame_rate, get_frame_count, get_aspect_ratio


# A simple way to just have a class w/ the contents we need to operate dandere2x

class VideoSettings:

    def __init__(self, ffprobe_dir, video_file: str):
        """
        A simple class to get the video settings needed for dandere2x using ffprobe.
        """

        self.ffprobe_dir = ffprobe_dir
        self.settings_json = get_video_info(self.ffprobe_dir, video_file)
        self.frame_count = int(get_frame_count(self.ffprobe_dir, video_file))

        # todo: This entire class can be removed and simplified into the 'except' clause,
        # but having this try / except provides me a sense of security. Some file containers
        # Won't work for the first try, and some won't work for the except, so there's double security here?
        try:
            self.height = self.settings_json['streams'][0]['height']
            self.width = self.settings_json['streams'][0]['width']
            self.frame_rate = float(Fraction(self.settings_json['streams'][0]['r_frame_rate']))
            self.dar = self.settings_json['streams'][0]['display_aspect_ratio']

        except KeyError:
            print("key error")
            self.width, self.height = get_width_height(self.ffprobe_dir, video_file)
            self.frame_rate = float(Fraction(get_frame_rate(self.ffprobe_dir, video_file)))
            self.dar = get_aspect_ratio(self.ffprobe_dir, video_file)

        # horizontal videos often do not include rotate so this is separated to keep up the performance
        try:
            self.rotate = int(self.settings_json['streams'][0]["tags"]["rotate"])
        except KeyError:
            self.rotate = int(0)