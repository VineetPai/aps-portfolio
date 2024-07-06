# Loading Video
For a user to watch/stream video on his favorite platform his device needs to load that video from the platforms servers where it is stored.
Watching can be done is two ways
1 download whole video
2 load in parts(streaming)

- Downloading the whole video has several disadvantages:
  - User has to wait until the entire video is downloaded.
  - User cannot switch between different video quality options.
  - If the user loses interest midway, the downloaded parts go unused.
  - Takes up space on the user's device; some videos can be hours long and several GBs in size.
Hence streaming is better than downloading whole video.

## Measures to make streaming better
# Video transcoding
<!-- cisco code -->
<!-- https://github.com/cisco/openh264?tab=readme-ov-file -->

It is the process of converting a video file from one format to another. This involves decoding the original video file into an uncompressed format and then re-encoding it into the desired format. In this process metadata like thumbnail, title, description can also be embeded. 
![Video transcoding architecture](https://www.researchgate.net/publication/257879554/figure/fig2/AS:267897603883015@1440883174034/Architecture-of-video-transcoding.png)
