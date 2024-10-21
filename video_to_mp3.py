import moviepy
import moviepy.editor

video = moviepy.editor.VideoFileClip('aro.mp4')
audio = video.audio
audio.write_audiofile('audio.mp3')