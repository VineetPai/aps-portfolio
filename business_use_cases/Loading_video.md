# Loading Video

For a user to watch/stream video on his favorite platform his device needs to load that video from the platforms servers where it is stored.

**Watching can be done is two ways**

- download whole video
- load in parts(streaming)

**Downloading the whole video has several disadvantages:**

- User has to wait until the entire video is downloaded.
- User cannot switch between different video quality options.
- If the user loses interest midway, the downloaded parts go unused.
- Takes up space on the user's device; some videos can be hours long and several GBs in size.
  Hence streaming is better than downloading whole video.

# Measures to make streaming better

# 1.1 Video transcoding

It is the process of converting a video file from one format to another. This involves decoding the original video file into an uncompressed format and then re-encoding it into the desired format. In this process metadata like thumbnail, title, description can also be embeded.
![Video transcoding architecture](https://www.researchgate.net/publication/257879554/figure/fig2/AS:267897603883015@1440883174034/Architecture-of-video-transcoding.png)

- Benefits of video transcoding:
  - **Compatibility**: Ensures videos can be played on various devices and platforms by converting to supported formats.
  - **Streaming Efficiency**: Facilitates adaptive bitrate streaming, providing multiple quality options based on the viewer's internet connection and device capabilities.
  - **Storage Optimization**: Compresses video files to reduce their size, making storage more efficient and cost-effective.
  - **Broad Accessibility**: Makes content accessible to a wider audience by ensuring it can be viewed on different devices with varying technical specifications.
  - **Content Delivery**: Improves content delivery networks (CDNs) efficiency by providing optimized video formats for faster and more reliable distribution.

## Design techniques and Algorithms for Transcoding

### Huffman coding

It is an efficient method for data compression, minimizes total number of bits used to represent a set of data. It is a lossless compression technique, it creates a min-heap of characters based on there frequency in data.  
**Time Complexity:** O(nlog(n)), n=number of unique characters  
**Space Complexity:** O(n)  
[Implementation](https://github.com/Elzawawy/huffman-coding-zipper)

### H264

Also known as Advanced Video Coding (AVC), is a popular video compression standard used for compression and distribution of videos, it offers high compression efficiency, which reduced the bandwidth required for video streaming.  
**Encoding Complexity:** O(nlog(n)), n is number of pixels in a frame  
[Implementation](https://github.com/cisco/openh264?tab=readme-ov-file)

# 1.2 Use of CDNs

Content delivery networks are servers which stores the content near to users, hence reducing time required to load video. If a video resides in a server at palo alto, a CDN in mumbai will cache that video so whenever that video is accessed by any user in India, CDN will provide it.  
![CDN structure](https://blog.paessler.com/hubfs/cdn-orange.png)  
**Challenges:** finding nearest CDN

## Design techniques and Algorithms

### Dijkstra’s algorithm

If a network of CDN servers was created than Dijkstra's can be employed to get shortest path between client and them.  
Technique: Greedy approach, single source shortest path.  
**Time Complexity:** O((V + E) log V), where V is the number of vertices and E is the number of edges.  
**Space Complexity:** O(V), due to the storage requirements for the distance array and the set of visited nodes.  
[Implementation](https://github.com/mburst/dijkstras-algorithm)

### A\* search

A\* Search Algorithm: Greedy approach, heuristic based  
**Time Complexity:** O(E), where E is the number of edges in the graph.  
**Space Complexity:** O(V) auxiliary space in worst case.  
[Implementation](https://github.com/EinarUeland/Astar-Algorithm)
