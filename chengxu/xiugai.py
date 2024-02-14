import random
import shutil


def st(s,s2):
    for i in range(1,1100):
        str_num = str(i)  # 数字转化为字符串
        str_six_num = str_num.zfill(6)  # 字符串右对齐补0
        print(str_six_num)
        name='MOT16-'+s+'-'+str_six_num+'.txt'
        print(name)
        path="D:/download_edge/UA-DETRAC-G2/labels/"+s2+'/'+name
        print(path)
        res=[]
        try:
            with open(path,"r+") as f:
                lines = f.readlines()
                print(lines)
                for line in lines:
                    line=line.replace('0',"4",1)
                    res.append(line)
                print(res)
        except:
            print("错误")
            continue
        with open(path, "w+") as f:
            f.writelines(res)


def shanchu(s):
    test = random.sample(range(1, 1100), 200)
    for i in test:
        str_num = str(i)  # 数字转化为字符串
        str_six_num = str_num.zfill(6)  # 字符串右对齐补0
        print(str_six_num)
        name = 'MOT16-' + s + '-' + str_six_num + '.txt'
        name1 = 'MOT16-' + s + '-' + str_six_num + '.jpg'
        path = "D:/download_edge/UA-DETRAC-G2/images/" + 'train' + '/' + name1
        path0 = "D:/download_edge/UA-DETRAC-G2/images/" + 'val' + '/' + name1
        path1 = "D:/download_edge/UA-DETRAC-G2/labels/" + 'train' + '/' + name
        path2 = "D:/download_edge/UA-DETRAC-G2/labels/" + 'val' + '/' + name
        try:
            shutil.move(path0, path)
            shutil.move(path2, path1)
        except:
            print("失败")
    print(test)
shanchu('11')
shanchu("02")
shanchu("04")
shanchu("05")
shanchu("09")
shanchu("10")
shanchu("13")

# st("09","train")
# st("09","val")
# st("10","train")
# st("10","val")
# st("11","train")
# st("11","val")
# st("13","train")
# st("13","val")
# st("02","train")
# st("02","val")
# st("04","train")
# st("04","val")
