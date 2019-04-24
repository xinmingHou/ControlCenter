import os
    
def reName(dirname):
    for i in os.listdir(dirname):
        if os.path.splitext(i)[1] == '.png':
            name = i.split('.')  # 以 - 分割提取文件名
            print(i)
            print(os.path.splitext(i))
            num = name[0]
            newpath = dirname + str(int(num))+".png"
            oldpath = dirname + i
            os.rename(oldpath, newpath)

if __name__ == '__main__':
        dirname = 'mappics/'
        reName(dirname)
