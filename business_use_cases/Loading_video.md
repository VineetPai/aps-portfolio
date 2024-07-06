<!-- # Loading Video -->

For a user to watch/stream video on his favorite platform his device needs to load that video from the platforms servers where it is stored.
**Watching can be done is two ways**

- 1 download whole video
- 2 load in parts(streaming)

- Downloading the whole video has several disadvantages:
  - User has to wait until the entire video is downloaded.
  - User cannot switch between different video quality options.
  - If the user loses interest midway, the downloaded parts go unused.
  - Takes up space on the user's device; some videos can be hours long and several GBs in size.
    Hence streaming is better than downloading whole video.

# Measures to make streaming better

# Video transcoding

<!-- cisco code -->
<!-- https://github.com/cisco/openh264?tab=readme-ov-file -->

It is the process of converting a video file from one format to another. This involves decoding the original video file into an uncompressed format and then re-encoding it into the desired format. In this process metadata like thumbnail, title, description can also be embeded.
![Video transcoding architecture](https://www.researchgate.net/publication/257879554/figure/fig2/AS:267897603883015@1440883174034/Architecture-of-video-transcoding.png)

- Benefits of video transcoding:
  - **Compatibility**: Ensures videos can be played on various devices and platforms by converting to supported formats.
  - **Streaming Efficiency**: Facilitates adaptive bitrate streaming, providing multiple quality options based on the viewer's internet connection and device capabilities.
  - **Storage Optimization**: Compresses video files to reduce their size, making storage more efficient and cost-effective.
  - **Standardization**: Adheres to specific standards required by different platforms or broadcasting services.
  - **Enhanced Viewing Experience**: Enables smooth playback by converting videos into formats that support efficient streaming and buffering.
  - **Broad Accessibility**: Makes content accessible to a wider audience by ensuring it can be viewed on different devices with varying technical specifications.
  - **Content Delivery**: Improves content delivery networks (CDNs) efficiency by providing optimized video formats for faster and more reliable distribution.

## Algorithms for Transcoding

### Huffman coding

It is an efficient method for data compression, minimizes total number of bits used to represent a set of data. It is a lossless compression technique, it creates a min-heap of characters based on there frequency in data.
**Time Complexity:** O(nlog(n)), n=number of unique characters.
**Space Complexity:** O(n)
[Implementation](../codes/huffmanCode.py)

# Use of CDNs
