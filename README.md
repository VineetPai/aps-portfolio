<!-- # Video streaming platform Portfolio -->

<!-- <dl>
<dt>Course Name</dt>
<dd>Algorithmic Problem Solving</dd>
<dt>Course Code</dt>
<dd>23ECSE309</dd>
<dt>Name</dt>
<dd>Vineet Pai</dd>
<dt>University</dt>
<dd>KLE Technological University, Hubballi-31</dd>
</dl> -->

**Course Name:** Algorithmic Problem Solving  
**Course Code:** 23ECSE309  
**Name:** Vineet Pai  
**SRN:** 01FE21BCS273  
**University:** KLE Technological University, Hubballi-31  
**Portfolio domain:** Video streaming platform Portfolio

---

#### Note:

<!-- This page hosts:

1. <a href='# Introduction'>Introduction</a>
2. <a href='# Why this Portfolio?'>Why this Portfolio</a>
3. <a href='# Objectives'>Objectives</a>
4. <a href='# Design'>Design</a>
5. <a href='# Challenges'>Challenges</a>
6. <a href='# To-Do'>To-Do</a> -->

This page hosts:

1. [Introduction](#Introduction)
2. [Why this Portfolio](#why-this-portfolio)
3. [Objectives](#objectives)
4. [Design](#design)
5. [Challenges](#challenges)
6. [To-Do](#to-do)

---

# Introduction

The first websites were simple pages of text with maybe an image or two. Today, however, anyone with a fast enough Internet connection can watch high-definition movies or make a video call over the Internet. This is possible because of a technology called streaming.

Streaming is the continuous transmission of audio or video files from a server to a client. In simpler terms, streaming is what happens when consumers watch TV or listen to podcasts on Internet-connected devices. With streaming, the media file being played on the client device is stored remotely, and is transmitted a few seconds at a time over the Internet.[1]

# Why this Portfolio?

Video streaming is becoming extreamly popular nowdays and there is no fall in watch time in near future, todays kids are getting addicted to youtube videos, shorts, tiktok, insta reels etc. All of it containing videos at core. 80% of internet by size is video content and on average 17 hours of video is streamed every week by an internet user [2]. I personally use stream youtube videos 2-3 hours per day.
For businesses, the potential to reach consumers via online videos is high.

# Objectives

To improvise functions using algorithms and data structures

# Business use cases

1 [Loading video](business_use_cases/Loading_video.md)

2 Creating topic domains  
Topic domains are groups of related or identical videos organized into a hierarchical structure based on specific topics such as gaming, education, films, music, etc. Each domain can contain sub-domains and sub-sub-domains, creating a multi-level hierarchy.  
**Benefits:**  
Targeted Changes: If the platform needs to make changes to specific videos, the hierarchical structure allows for targeted modifications within a particular domain or sub-domain.  
Improved Recommendations: When users frequently watch videos from two different domains, the platform can recommend these videos to other users, enhancing the recommendation system.  
**Design techniques and Algorithms:**  
Graphs  
Nodes: Represent videos.  
Edges: Represent relationships between videos.  
Hierarchical Structure: Represented using parent-child relationships within the graph.  
**Time complexity:** O(1) for adding node.  
**Space complexity:** O(V + E) where V is the number of videos (nodes) and E is the number of relationships (edges)

3 Playing video  
While playing videos, segments need to be dynamically loaded from servers or CDNs. Users often switch between different sections of the video, requiring an efficient method to prioritize which segments to load. Using a heap with priority can help in selecting which segments to load based on various criteria such as chapters created by the artist, most viewed sections, and segments frequently jumped to by viewers.

Benefits  
Saving Time: Ensures quick access to important segments.
Efficient Use of Bandwidth: Prioritizes loading of segments that are more likely to be viewed.
Improved User Experience: Ensures that the most important segments are loaded first, reducing buffering time.
**Design techniques and Algorithms:**
Heap
**Time complexity:** O(log(n)) for getting next segment.  
**Space complexity:** O(n)

2 Search results
3 Recommendations

2 User engagement.
1 Creating domains.
2 Search results.
3 Recommendations.
4

# Design

# Challenges

# To-Do

# References

[1] Cloudflare
https://www.cloudflare.com/learning/video/what-is-streaming/  
[2]
https://www.oberlo.com/statistics/online-video-consumption-statistics
