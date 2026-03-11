from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(input_path, output_path):

    try:
        video = VideoFileClip(input_path)

        audio = video.audio

        audio.write_audiofile(output_path)

        audio.close()
        video.close()

        return True

    except Exception as e:
        print("Error:", e)
        return False