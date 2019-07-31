import subprocess,json,os
import cv2

#源文件目录
dir_path = 'E:/video-cut/source-file-mp4/'
#截取后的文件目录
put_path = 'E:/video-cut/video-slip/'
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

# 获取视频时长
def get_file_dura_time(file_name):
    pname = 'ffprobe -v quiet -print_format json -show_format "%s"' % (file_name)
    result = subprocess.Popen(pname, shell=False, stdout=subprocess.PIPE).stdout
    list_std = result.readlines()
    str_tmp = ''
    for item in list_std:
        str_tmp += bytes.decode(item.strip())
    json_data = json.loads(str_tmp)
    # 获取时长，格式是str
    dura_time = json_data['format']['duration']
    # 因为时长精确到毫秒，是str格式，转成float类型
    dura_time_float = float(dura_time)
    return dura_time_float



#获取视频帧率
def get_file_frame_cv(file_name):
    video = cv2.VideoCapture(file_name);

    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

    if int(major_ver) < 3:
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else:
        fps = video.get(cv2.CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
    video.release();
    return fps;


#定义方法，传入文件和截取的时间信息，调用ffmpeg进行切割
def cut_media_time(file_name,start_time,cut_time,put_path,index):
    # 获取文件名，去掉路径
    filename = os.path.split(file_name)[1]
    #去掉后缀名，重新生成文件名
    filename = os.path.splitext(filename)[0] + '_' + str(index) + os.path.splitext(filename)[1]
    #合并到路径里
    put_file_path = os.path.join(put_path, filename)
    # ffmpeg的字符串切割命令字符串,使用关键帧
    pfile = 'ffmpeg -ss "%s" -t "%s" -i "%s" -vcodec copy -acodec copy "%s"'%(get_format_time(start_time),get_format_time(cut_time),file_name,put_file_path)

    #不使用关键帧
    # pfile = 'ffmpeg -ss "%s" -t "%s" -i "%s" -c:v mpeg4 -c:a copy "%s"' % (get_format_time(start_time), get_format_time(cut_time), file_name, put_file_path)

    #执行切割操作
    subprocess.Popen(pfile)

#秒变为00:00:00时间格式
def get_format_time(time):
    m, s = divmod(time, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

#创建存放切割后视频文件的路径
def create_folder(file_name,put_path):
    # 获取文件名
    filename = os.path.split(file_name)[1]
    # 去掉后缀名，作为新的文件名
    put_file_name = os.path.splitext(filename)[0]
    # 合并路径作为切分后视频的路径
    put_file_path = os.path.join(put_path, put_file_name)
    # 路径若不存在则新建路径
    if not os.path.exists(put_file_path):
        os.makedirs(put_file_path)
    return put_file_path

#设置切割视频的时间，循环切割
def set_cut_time(file_name,put_path,time_frame):
    dura_time_float = get_file_dura_time(file_name)
    #计算每秒的帧数
    # fps = get_file_frame_cv(file_name)
    count = int(dura_time_float / time_frame)
    #创建存放文件的路径
    put_file_path = create_folder(file_name,put_path)
    i = 0
    while i < count:
        start_time = i * time_frame
        i += 1
        cut_media_time(file_name,start_time,time_frame,put_file_path,i)
    start_time = count * time_frame
    cut_media_time(file_name,start_time,time_frame,put_file_path,count+1)

#视频转为MP4
def transfer_video(file_name):
    put_path_mp4 = 'E:/video-cut/source-file-mp4'
    # 获取文件名
    filename = os.path.split(file_name)[1]
    print(filename)
    # 去掉后缀名，作为新的文件名
    put_file_name = os.path.splitext(filename)[0] + '.mp4'
    # 路径若不存在则新建路径
    if not os.path.exists(put_path_mp4):
        os.makedirs(put_path_mp4)
    put_file_name = os.path.join(put_path_mp4,put_file_name)
    pfile = 'ffmpeg -i "%s" -c:v libx264 -strict -2 -s 1980x1080 -b 1000k "%s"'%(file_name,put_file_name)
    subprocess.Popen(pfile)

#计算切分成等长小视频，每个小视频结束多几秒钟，最后一个小视频可小于规定长度
get_all_file(dir_path)
#对列表中的文件批量执行
for file in file_list:
    # transfer_video(file)
    set_cut_time(file,put_path,300.00)


