The project will provide basic animation capabilities through programming.
The following steps will implement this project.
1. ffmpeg -i video.mp4; will be used to extract the frames as images from a video and place them in a folder.
2. The python program will then go over the frames and alter them.
3. ffmpeg -i frame%d.jpg; will be used to compose the frames into a video. 
*Lots of options exist for steps 1 and 3. The most important being frames extracted for each second of video and how many frames will be pressed into every second of video.
*The heftiest part of the process is step 2 where the possibilities are almost endless and will inevitably require a lot of math. Rasterization and geometry is a good place to start.

The example here has 30.12 frames per second. For now try to keep the same going in and out. So 30

All commands begin at C:\Users\Kendrick\PycharmProjects\FFMPEG_Animation\Videos
Extract frames
ffmpeg -i Original_blank.mp4 -vf fps=30.12 Frames/output%06d.png

Compile frames into video
ffmpeg -framerate 30.12 -i Frames\output%06d.png -c:v libx264 -r 30.12 output.mp4
//For some reason the above can only be played by vlc player perhaps the codec libx264 is to blame


Sources:
Video to frames
https://medium.com/@alibugra/extract-frames-as-an-image-from-video-files-using-ffmpeg-65b52d3d97db#:~:text=%24%20ffmpeg%20-i%20video.mp4%20-vf%20fps%3D1%20img%2Foutput%2506d.png%20In,means%20every%20minute%2C%20fps%3D1%2F600%20means%20every%20ten%20minutes.

Frames to video
https://shotstack.io/learn/use-ffmpeg-to-convert-images-to-video/#:~:text=Create%20a%20slideshow%20video%20from%20a%20sequence%20of,Adding%20transition%20effects%20to%20the%20video%20slideshow.%20

Lots of video encoding codecs are available here are some.
Codec name (short)	Full codec name	Container support
AV1	AOMedia Video 1	MP4, WebM
AVC (H.264)	Advanced Video Coding	3GP, MP4
H.263	H.263 Video	3GP
HEVC (H.265)	High Efficiency Video Coding	MP4
MP4V-ES	MPEG-4 Video Elemental Stream	3GP, MP4
MPEG-1	MPEG-1 Part 2 Visual	MPEG, QuickTime
MPEG-2	MPEG-2 Part 2 Visual	MP4, MPEG, QuickTime
Theora	Theora	Ogg
VP8	Video Processor 8	3GP, Ogg, WebM
VP9	Video Processor 9	MP4, Ogg, WebM

The codecs can vary wildly in compilation time.


Special effect commands examples.
Black Rainbow-> 0,339,rainbow,2
Adding Text->