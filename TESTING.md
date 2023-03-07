## Table of Contents

* [Testing](#testing)
  * [Test 1](#test-1)
  * [Test 2](#test-1)
  * [Test 3](#test-1)

## Testing

Large Tests to Perform:

  Bots:

* Automate the recordings and delete recordings accordingly on the system.
* Create a file system topology that can be used for the website to improve the UI/UX design.

  FFMPEG:
* Saving an mp4 file to an s3 bucket and downloading it from the website
* Selecting a portion of an mp4 file from an s3 bucket and downloading.

### Challenges

* File storage
* Recording 24/7 hr streams
* Automation
* FFMPEG use on HTML headers
* Data translation from file storage to the Front-End

CloudFront added in front of S3 (will need to be able to go through CloudFront to get data)

### Tests

#### Test 1

- Checking file formatting in S3 with Dollymount (clone of the real stream on the testing server).

  1. Created an S3 bucket and EC2 with AntMediaServer installed.
  2. Added S3 bucket credentials to the AMS server.

  | Image/ Code                                                                                                                                                                                                    | Result                                                                                                                                                                           | Considerations                                                                                                                                                                   | Additional                                                                                                                |
  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
  | ![test file formatting](https://file+.vscode-resource.vscode-cdn.net/Users/avstarsystems/Dropbox/AV%20STAR%20SYSTEMS/avss-software-engineering/GItHub/mp4-url-recorder/documentation/tests/test-1-formatter.png) | I added the credentials and tested recording a stream and these are the results. Saves in multipe formats, need to decipher whats needed for FFMPEG to parse.                    | Removal of additional files possibly not needed. Files definitely need to be time stamped. MP4 file only shows once the stream has stopped (or incase of 24/7 stream is stopped) | The folder architecture of 1 - 31 days will have to be looked at as it's unclear if this can be done from the AMS server. |
  | ![test file storage](https://file+.vscode-resource.vscode-cdn.net/Users/avstarsystems/Dropbox/AV%20STAR%20SYSTEMS/avss-software-engineering/GItHub/mp4-url-recorder/documentation/tests/test-1-storage.png)      | After uploading to S3 bucket the storage goes down properly to 24.1MB, it went up as I turned it back on                                                                         | local storage won't be impacted with multiple stream recording as AMS will delete files once completed and sent to S3                                                            | This significantly reduces resource consumption on the server                                                             |
  | ![test cpu usage](https://file+.vscode-resource.vscode-cdn.net/Users/avstarsystems/Dropbox/AV%20STAR%20SYSTEMS/avss-software-engineering/GItHub/mp4-url-recorder/documentation/tests/test-1-cpu.png)             | One stream recording and cpu is responding well. Will need a larger test peformed on the production server to gather more information but I suspect an upgrade to be possible... |                                                                                                                                                                                  |                                                                                                                           |

#### Test 2

- Creating a script to pull an mp4 file from the S3.

  | Image/Code                                                                                                                                                                                               | Result                                                             | Considerations                                                                         | Additional                                                                                                                                                                           |
  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | ![test recording](https://file+.vscode-resource.vscode-cdn.net/Users/avstarsystems/Dropbox/AV%20STAR%20SYSTEMS/avss-software-engineering/GItHub/mp4-url-recorder/documentation/tests/test-2-recording.png) | successfully got 2 minutes of a stream using ffmpeg-python package | package is highly accessible, easy to read and small enough to parse in a few minutes. | The base structure for downloading with URLs is built, however, the front end complicates the design. Needs additional information such as the file architecture issue to be sorted. |
  |                                                                                                                                                                                                          |                                                                    |                                                                                        |                                                                                                                                                                                      |

An example code is written below.

```

FROM = '00:00:00'

TO = '00:02:00'

name_of_new_file = 'test.mp4'

ffmpeg.input(url_to_download, ss=FROM, t=TO).output(

    name_of_new_file, vcodec='copy', acodec='copy').overwrite_output().run()

```

What does this mean?

Well, it means the metadata we need is attached to the mp4 file and that's excellent for getting the recordings. This code can be adapted to calculate the time difference. The total time of the file will need to extract to help determine ranges for the user to trim.

It also means we don't need to download the whole file each time we need a selection from an mp4 file.

#### Test 3

- Running a python script in the background continuously as a cron job

Link to material for cronjob [here](https://medium.com/analytics-vidhya/easiest-way-to-run-a-python-script-in-the-background-4aada206cf29#:~:text=The%20easiest%20way%20of%20running,can%20use%20Windows%20Task%20Scheduler.&text=You%20can%20then%20give%20the,by%20giving%20the%20time%20particulars.).

This test includes writing a script to send an email every 5 minutes to a new email address. By running it constantly we can help prove this functionality and consider it as the feature of the project. Specifically, the automation elements require moving files and updating a front-end database.

Each test will help prove the functionality of each feature as a whole in the project.

Cronjobs are processes that run in the background and they specify how often to run each process that's created as a cronjob.

![Test 3 - Cron Job](documentation/tests/test-3-cronjob.png)

What I'm specifically testing is if I run a cronjob on a file does that file have access to the rest of the files in that folder. We can test this by creating a script and importing another file in the same directory to perform actions on. For example, sending emails.

| Image/Code                                                                                                                                                                                                   | Result                            | Considerations                                                  | Additional                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Test 3 - Cron Job](https://file+.vscode-resource.vscode-cdn.net/Users/avstarsystems/Dropbox/AV%20STAR%20SYSTEMS/avss-software-engineering/GItHub/mp4-url-recorder/documentation/tests/test-3-linux-cron.png) | Testing with linux cronjob failed | possibly doesn't have the required permissions to work properly | Checking alternative packages and options for cron jobs within the Django application. Important to get working as it will solve major issues with automation. |
|                                                                                                                                                                                                              |                                   |                                                                 |                                                                                                                                                                |

[Back to Top](#table-of-contents)
