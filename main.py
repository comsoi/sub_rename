import os


def get_file_name(path):
    filetypeList = ['.mkv', '.mp4']  # 视频扩展名
    filenameList = []
    subtypeList = ['.ass', '.ssa', '.srt', '.sup']  # 字幕扩展名
    subtitleList = []
    subtype = []
    filelist = os.listdir(path)
    for filename in filelist:
        filetype = os.path.splitext(filename)[1]
        filename = os.path.splitext(filename)[0]
        if filetype in filetypeList:
            filenameList.append(filename)  # 返回mkv mp4文件名（不包含扩展名）
        elif filetype in subtypeList:
            subtitleList.append(filename)  # 返回字幕文件名（包含扩展名）
            subtype.append(filetype)
    return filenameList, subtitleList, subtype


def rename(filenameList, subtitleList, subtype):
    for i, filename in enumerate(subtitleList):  # 遍历所有字幕文件
        newName = os.path.join(filenameList[i]+subtype[i])
        oldName = os.path.join(filename+subtype[i])
        os.rename(oldName, newName)


# 若main()函数无输入则path为脚本所在目录
def main(path=os.path.split(os.path.realpath(__file__))[0]):
    os.chdir(path)
    filename_list, subtitle_list, subtype = get_file_name(path)
    rename(filename_list, subtitle_list, subtype)


if __name__ == '__main__':
    main()
    print(os.path.split(os.path.realpath(__file__))[0])
