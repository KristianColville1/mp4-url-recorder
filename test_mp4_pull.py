import ffmpeg
import os

url_to_download = 'https://churchcamlive-recordings.s3.eu-west-1.amazonaws.com/streams/d_test-2023-03-06_11-34-30.440.mp4'
FROM = '00:00:00'
TO = '00:02:00'
name_of_new_file = 'test.mp4'
ffmpeg.input(url_to_download, ss=FROM, t=TO).output(
    name_of_new_file, vcodec='copy', acodec='copy').overwrite_output().run()
