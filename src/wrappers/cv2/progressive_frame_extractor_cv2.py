import cv2
import os

from dandere2xlib.utils.dandere2x_utils import rename_file_wait

class ProgressiveFramesExtractorCV2:
    """
    Temporally extract frames from a video each time next_frame is called.
    Saves into dandere2x's inputs DIR.
    """

    def __init__(self, context):
        self.pre_processed_video = context.pre_processed_video
        self.input_frames_dir = context.input_frames_dir
        self.compressed_moving_dir = context.compressed_moving_dir
        self.compressed_static_dir = context.compressed_static_dir

        self.quality_minimum = context.quality_minimum
        self.quality_moving_ratio = context.quality_moving_ratio

        self.cap = cv2.VideoCapture(self.pre_processed_video)

        self.count = 1

    def extract_frames_to(self, stop_frame: int):

        for x in range(1, stop_frame):
            self.next_frame()

    def release_capture(self):
        self.cap.release()
        # Closes all the frames
        cv2.destroyAllWindows()

        # TODO: need to apply core d2x filters # FIXED: FFMPEG WORKAROUND
    def next_frame(self):
        """ Call and save the next frame. """

        success = False

        while not success:
            success, image = self.cap.read()

        if success:
            cv2.imwrite(self.input_frames_dir + "frame_temp_%s.jpg" % self.count, image, [cv2.IMWRITE_JPEG_QUALITY, 100])
            cv2.imwrite(self.compressed_static_dir + "compressed_temp_%s.jpg" % self.count, image,
                        [cv2.IMWRITE_JPEG_QUALITY, self.quality_minimum])
            cv2.imwrite(self.compressed_moving_dir + "compressed_temp_%s.jpg" % self.count, image,
                        [cv2.IMWRITE_JPEG_QUALITY, self.quality_minimum])

            rename_file_wait(self.input_frames_dir + "frame_temp_%s.jpg"  % self.count,
                             self.input_frames_dir + "frame%s.jpg" % self.count)

            rename_file_wait(self.compressed_static_dir + "compressed_temp_%s.jpg" % self.count,
                             self.compressed_static_dir + "compressed_%s.jpg" % self.count)

            rename_file_wait(self.compressed_moving_dir + "compressed_temp_%s.jpg" % self.count,
                             self.compressed_moving_dir + "compressed_%s.jpg" % self.count)

            self.count += 1

