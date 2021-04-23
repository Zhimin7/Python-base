import os

src = './p2'
target = './p3'


def copy(src, target):
    # 判断是否是文件夹
    if os.path.isdir(src) and os.path.isdir(target):
        filelist = os.listdir(src)  # 列出该文件夹下的所有文件---》返回一个列表
        # 将每一个文件遍历出来
        for file in filelist:
            filepath = os.path.join(src, file)  # 写出文件名
            if os.path.isdir(filepath):     # 判断是否存在文件夹
                target_dir = os.path.join(target, file)
                print(target_dir)
                os.mkdir(target_dir)
                copy(src, filepath)
            else:
                with open(filepath,mode='r') as f:
                    container = f.read()
                    target_file_path = os.path.join(target, file)
                    with open(target_file_path,'w') as f:
                        f.write(container)


copy(src, target)
print('复制完成')