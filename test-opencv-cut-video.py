import cv2
import os
import datetime

#源文件目录
dir_path = 'E:/video-cut/source-file/'
#截取后的文件目录
put_path = 'E:/video-cut/video-slip/'
#定义个列表存放每个文件路径，便于后期操作
all_vedio_file=[]

#获取所有文件
def get_all_file(dir_path):
    for file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file)
        if os.path.isdir(file_path):
            get_all_file(file_path)
        else:
            all_vedio_file.append(file_path)

#视频切割
def cut_video(file):
    video_capture = cv2.VideoCapture(file)
    #FPS帧率
    fps = video_capture.get(5)
    #总帧数
    all_frams = video_capture.get(7)
    print('fps:',fps)
    print('总帧数:', all_frams)
    # 视频的宽和高
    size = (int(video_capture.get(3)), int(video_capture.get(4)))
    print('视频的宽和高：',size)
    #视频段为10s
    cut_time = 60
    # 当前帧
    frame_index = 0
    # 当前截取的第几段
    flag = 0
    success, bgr_image = video_capture.read()
    fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')


    # 获取文件名，去掉路径
    filename = os.path.split(file)[1]
    put_file_path = os.path.join(put_path,os.path.splitext(filename)[0])
    # 路径若不存在则新建路径
    if not os.path.exists(put_file_path):
        os.makedirs(put_file_path)
    # 去掉后缀名，重新生成文件名
    put_file_name = os.path.splitext(filename)[0] + '_' + str(flag) + os.path.splitext(filename)[1]
    # 合并到路径里
    put_file_name = os.path.join(put_file_path, put_file_name)
    v = cv2.VideoWriter(put_file_name, fourcc, fps, size)

    while success:  # 循环读取视频帧

        cv2.imshow('frame', bgr_image)

        if v.isOpened():
            v.write(bgr_image)

        if frame_index == (fps * cut_time) * flag:
            v = cv2.VideoWriter(os.path.join(put_file_path,os.path.splitext(filename)[0] + '_' + str(flag) + os.path.splitext(filename)[1]), fourcc, fps, size)
            flag += 1
        success, bgr_image = video_capture.read()
        frame_index = frame_index + 1

    video_capture.release()
    v.release()



start_time = datetime.datetime.now()
get_all_file(dir_path)
for file in all_vedio_file:
    cut_video(file)
end_time = datetime.datetime.now()
print(end_time - start_time)