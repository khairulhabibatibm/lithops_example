import lithops
import ffmpeg
from storage_util import upload_file

def process_video(output_name):
    input = ffmpeg.input('http://techslides.com/demos/sample-videos/small.mp4')
    audio = input.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
    video = input.video.hflip()
    out = ffmpeg.output(audio, video, 'output.mp4')
    ffmpeg.run(out)
    f = open('output.mp4','rb')
    upload_file("test-bucket-fn",output_name,f)
    print('finish uploading')
    f.close()

if __name__ == '__main__':
    fexec = lithops.FunctionExecutor()
    fexec.call_async(process_video,'output.mp4')
    print(fexec.get_result())


# http://techslides.com/demos/sample-videos/small.mp4

