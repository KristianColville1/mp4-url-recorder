import ffmpeg
import os
import json


def get_recording_duration(url):
    """ Gets the duration of the recording url and converts it into the req"""
    json_text = ffmpeg.probe(url)

    dict_to_json = json.dumps(json_text)
    json_file = open('test.json', 'w')
    json_file.write(dict_to_json)
    json_file.close()


def get_recording(url, start, end, new_file_name):
    """ 
    Takes the recording information and downloads and saves the file
    """
    url_to_download = 'name of recording file url'
    FROM = '00:00:00'
    TO = '00:02:00'
    name_of_new_file = 'test.mp4'

    ffmpeg.input(url_to_download, ss=FROM, t=TO).output(
        name_of_new_file, vcodec='copy', acodec='copy').overwrite_output().run()
