import subprocess,os
import cv2

#源文件目录
dir_path = 'E:/video-cut/source-file/'
#转为mp4的文件目录
dir_mp4_path = 'E:/video-cut/source-file-mp4/'
#定义个列表存放每个文件路径，便于后期操作
file_list=[]

#创建个方法，统计每个文件路径，并追加列表中。用到了递归，列表中的是每个文件的绝对路径
def get_all_file(dir_path):
    for file in os.listdir(dir_path):
        filepath = os.path.join(dir_path, file)
        if os.path.isdir(filepath):
            get_all_file(filepath)
        else:
            file_list.append(filepath)


#视频转为MP4
def transfer_video(file_name):
    # 获取文件名
    filename = os.path.split(file_name)[1]
    print(os.path.splitext(filename)[1])
    if os.path.splitext(filename)[1] == '.mp4':
        return
    # 去掉后缀名，作为新的文件名
    put_file_name = os.path.splitext(filename)[0] + '.mp4'
    video_capture = cv2.VideoCapture(file)
    # 视频的宽和高
    width = int(video_capture.get(3))
    height = int(video_capture.get(4))
    put_path_mp4 = 'E:/video-cut/source-file-mp4'

    # 路径若不存在则新建路径
    if not os.path.exists(put_path_mp4):
        os.makedirs(put_path_mp4)
    put_file_name = os.path.join(put_path_mp4,put_file_name)
    # pfile = 'ffmpeg -i "%s" -vf scale=%s:%s "%s"'%(file_name,width,height,put_file_name)
    pfile = 'ffmpeg -i "%s" "%s"'%(file_name,put_file_name)
    subprocess.Popen(pfile)


# 转码MP4
get_all_file(dir_path)
for file in file_list:
    transfer_video(file)
