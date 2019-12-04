try:
    import util
except:
    from . import util
from collections import  defaultdict
class SPI (object):
    def __init__(self, raindata,dates,scales):
        self.scales=scales
        self.rain=raindata
        self.dates=dates
    def calculate(self, fit=util.gammafit):
        spiData=defaultdict(list)
        spiData["date"]=self.dates
        for scale in self.scales:
            print("scale\t",scale)
            raindata=util.summov(self.rain,scale)
            dates2=self.dates[scale-1:]
            global spi
            spi,groupdate=util.group(raindata,dates2,func=util.SPI_function, fit=fit)
            lags= [float("nan") for i in range(scale-1)]
            for i in lags+spi:
                spiData[scale].append(i)
        self.fields=spiData.keys()
        print("Done")
        return spiData

##import sys
##script = sys.argv[0]
##infile = sys.argv[1]
##outfile = sys.argv[2]
##    
####infile='data/Rain.csv'
####outfile='SPI_total1.csv'
##scales=sys.argv[3:]
##if len(infile)==0 or len(outfile)==0 or  len(scales)==0:
##    print( "spi infile outfile scale1 scale2 scale3 ...")
##
##    



def main():
    import sys
    # make sure there are at least three arguments
    if  len(sys.argv) >=6:
        script = sys.argv[0]
        infile = sys.argv[1]
        raincol ,datecol= sys.argv[2], sys.argv[3]
        outfile = sys.argv[4]
        scales=sys.argv[5:]
        scales=map(int,scales)
        data=util.readcsv(infile)
        rain,dates=data[raincol],data[datecol]
        myspi=SPI(rain,dates,scales).calculate()
        util.write(myspi,outfile)
        print ('SPI is calcualted and saved in {}'.format(outfile))
    else:
        print ("\nUsage: spi  <infile> <rain col> <date col>\
<outfile> <scale>\n")
        print ("Example: spi  d:/Rain.csv  Rain \
date d:/spi.csv 1 3 6 9 12 24\n")
        #sys.exit(2)
if __name__ == '__main__':
    main()
    
##    import util
##    infile="data/commadelimited_monthly_wdates.csv"
##    data=util.readcsv(infile)
####    from datetime import timedelta,datetime
####    import random
####    random.seed(1234)
####    n=15
####    rain=[random.randint(1,50) for i in range(12*n)]
####    dates=[]
####    for y in range(n):
####        for m in range(12):
####           dates.append(datetime(2000+y,m+1,1))
##    scale=[1,3,6]
##    rain=data["Rain"]
##    date=data["date"]
##    myspi=SPI(rain,date,scale)
##    data=myspi.calculate(util.gammafit)
##    util.write(data,"data/spi.csv")
####    
##    
##
## 
##    # exclude script name from the argumemts list and pass it to main()
##    main()#sys.argv[1:])
    

