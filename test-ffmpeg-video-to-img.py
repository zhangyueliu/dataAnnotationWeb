from ffmpy import FFmpeg
import os,subprocess
from tqdm import tqdm

#对小视频进行抽帧，得到图片组
def cut_change(video_path,out_path,fps_r):
    """
    操作ffmpeg执行
    :param video_path: 处理输入视频流
    :param fps_r: 对视频帧截取速度
    :return:
    """
    # ff = FFmpeg(inputs={video_path:None},outputs={out_path: '-f image2 -vf fps=fps={}'.format(fps_r)})

    #清晰度较高
    ff = FFmpeg(inputs={video_path: None},
                outputs={out_path: '-f image2  -vf fps=fps={} -qscale:v 2'.format(fps_r)
                         })

    ff.run()


# 视频的绝对路径和图片存储的目标路径
def extract_frames(src_path, target_path):
    new_path = target_path

    for video_name in tqdm(os.listdir(src_path)):
        filename = os.path.join(src_path,video_name)
        cur_new_path = os.path.join(new_path , video_name.split('.')[0] + '/')
        if not os.path.exists(cur_new_path):
            os.mkdir(cur_new_path)
        dest = os.path.join(cur_new_path , video_name.split('.')[0] + '_%04d.jpg')
        #抽帧
        cut_change(filename,dest,8)

        #抽帧命令行
        # subprocess.Popen("D:/SoftWare/ffmpeg-20190722-817235b-win64-static/bin/ffmpeg.exe -i {0} -f image2 -vf fps=fps=10 {1}".format(filename,dest))


        #抽取关键帧
        # subprocess.Popen('ffmpeg -i {0} -vf select="eq(pict_type\,I)" -vsync 2 -s 1980x1080 -f image2 {1}'.format(filename,dest))
        # subprocess.call(["ffmpeg", "-i", filename, "-r", "8", dest])  # 这里的5为5fps，帧率可修改
        break;

extract_frames(src_path='E:/video-cut/video-slip/(101)_20190620202150_2',target_path='E:/video-cut/video-to-img')