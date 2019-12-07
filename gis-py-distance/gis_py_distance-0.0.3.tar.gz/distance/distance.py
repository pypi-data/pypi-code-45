
# 此类是读取dat，并分析dat文件中所有点离(x,y)距离的类
class Distance():
    # 初始化函数
    def __init__(self,p,x,y):
        self.a=input('请输入一个距离：')
        self.lines=self.readDat(p) #读取dat文件
        self.x=x
        self.y=y

    # 改造print函数
    def updatePrint(self,s):
        print(s)
        print("***********************************************************")

    #*********************************************************************

    # 读取dat文件，并存入一个数组里面
    def readDat(self,filePath):
        f=open(filePath,'r')
        lines=f.readlines() # 此行代码是把文件xyz.dat数据读成数组
        self.updatePrint("xyz.dat文件里有%s行数据"%len(lines))
        return lines

    #********************************************************************

    # 读取每行数据，并处理
    def execLine(self,line):
        name=line.split(',')[0]
        x=line.split(',')[1]
        y=line.split(',')[2]
        xy=((float(x)-self.x)**2+(float(y)-self.y)**2)**0.5
        return name,x,y,xy

    #********************************************************************

    # 判断坐标是否在距离之内
    def isInclude(self,**info):
        if info['distance']>float(self.a):
            self.updatePrint('点%s在距离之外'%info['mingzi'])
        elif info['distance']==float(self.a):
            self.updatePrint('点%s等于距离'%info['mingzi'])
        else:
            self.updatePrint('点%s在距离之内'%info['mingzi'])

    #********************************************************************

    def run(self):
        for line in self.lines:
            name,x,y,xy=self.execLine(line) # 读取每行数据并处理
            self.updatePrint('点名是:%s,x是:%s,y是%s,距离是:%s'%(name,x,y,xy))
            self.isInclude(distance=xy,mingzi=name) # 判断点是否在距离内
