# Production Server Guide

## Table of contents

* [Reasons](#reasons)
* [Options](#options)
* [Solutions](#solutions)

After the first experience with setting up the recording capability on the production server it failed to work properly and caused disruptions.

### Reasons

<hr>

The version of Ant Media Server we are currently using is 2.5.3 and there is a known bug with the streams folder. This bug is not set to be fixed until version 2.5.6 .

Development is not finished so the development server for testing is needed.

### Options

<hr>

Set up a new development server to avoid disruptions.

### Solutions

Build EC2 to replicate production server and test components.

Closest build and cost:
t3.large
4cpu
16 RAM

costs $0.1632 per hour left on

Turn off production server in between tests.

### Testing the Development Server

1. Set up EC2
2. Add one stream to server
3. Attach Ant Media to the S3 bucket
4. record an incoming stream for 2 hours
5. Check data is inside the S3.
6. Build the python project to collect the stream using ffmpeg.
7. Record all steps and changes made for replication on production server.
8. Visit the testing documentation for updates on components tested.
