from ffmpy import FFmpeg
import os
import PIL as Image
from tqdm import tqdm
import subprocess


def cut_change(video_path,out_path, out_path2, out_path3, base_path, fps_r):
    """
    操作ffmpeg执行
    :param video_path: 处理输入视频流
    :param out_path: 合成缩略图 10*10
    :param out_path2: 封面图路径
    :param out_path3: 合成Ts流和 *.m3u8文件
    :param base_path:
    :param fps_r: 对视频帧截取速度
    :return:
    """
    ff = FFmpeg(inputs={video_path:None},
                outputs={out_path: '-f image2 -vf fps=fps={},scale=180*75,tile=10x10'.format(fps_r),
                         out_path2: '-y -f mjpeg -ss 0 -t 0.001',
                         None: '-c copy -map 0 -y -f segment -segment_list {0} -segment_time 1  -bsf:v h264_mp4toannexb  {1}/cat_output%03d.ts'.format(
                             out_path3, base_path),
                         })
    print(ff.cmd)
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
        subprocess.Popen("C:/Users/zhangyue/Desktop/ffmpeg-20190722-817235b-win64-static/bin/ffmpeg.exe -i {0} -f image2 -vf fps=fps=1 {1}".format(filename,dest))

        # call(["ffmpeg", "-i", filename, "-r", "5", dest])  # 这里的5为5fps，帧率可修改


extract_frames(src_path='E:/video-cut/video-slip/(101)_20190620202150_2',target_path='E:/video-cut/video-to-img')