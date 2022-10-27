import datetime 
#from datetime import datetime
import sys
import getopt

if(__name__=="__main__"):
    day=""
    month=""
    year=""
    time=[]
    new_york=datetime.datetime.now()
    delhi=datetime.timedelta(hours=9)+datetime.timedelta(minutes=30)
    london=datetime.timedelta(hours=5)
    delhi=new_york+delhi
    london=new_york+london
    print(delhi.strftime("Delhi :: %A %d %B %Y --> %H:%M:%S "))
    print(london.strftime("London :: %A %d %B %Y --> %H:%M:%S "))
    argv=sys.argv[1:]

    try: 
        opts, args=getopt.getopt(argv,"d:m:y:t::")
    except:
        print("Error was wrong")

    for opt, arg in opts:
        if opt in ['-d']:
            day=arg
        elif opt in ['-m']:
            month=arg
        elif opt in ['-y']:
            if arg:
                year=arg
            else:
                year=datetime.datetime.now().year
        elif opt in ['-t']:
                time=arg.split(":")
                if len(time)!=2:
                    print("There is problem in time given")
                    exit(1)
    print("{} , {} , {} , {} ".format(day,month,year,time))
    print(datetime.datetime(year=int(year),month=int(month),day=int(day),hour=int(time[0]),minute=int(time[1])))
