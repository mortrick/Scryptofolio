# This fuction receive data from web API and store it in the DB
import urllib
import MySQLdb
import datetime

# Define Time

db = MySQLdb.connect("localhost","bot","bobo123","charts")
dt = datetime.datetime.now()
dt = str(dt)[0:16]
print "Executed at " + dt
# url = "https://api.cryptowat.ch/markets/bitfinex/btcusd/price"


def clean(link):

    cleanlink = link.replace("'","").replace("(","").replace(")","").replace(",","")
    if (len(link)<=5):
        cleanlink[0:1]
        return cleanlink[0:1]
    else:
        return cleanlink
        print cleanlink




# Input Group , linkID
# Output link
def getlinks(LinkGroupID,LinkID):
    c = db.cursor()
    sql = "SELECT Link FROM charts.links_to_download WHERE LinkGroupID = " +str(LinkGroupID) + " AND LinkID = " + str(LinkID)
    print sql
    c.execute(sql);
    for (Link) in c:
        Link = "{}".format(Link)
        ClLink = clean(Link)
        c.close()
        print
        "Download from " + ClLink
    return str(ClLink)


#Input Link
#Output Coin value
def getbtcval(LinkGroupID,LinkID):
    response = urllib.urlopen(getlinks(LinkGroupID,LinkID))
    coinjson = response.read()
    getCoinval = coinjson[19:23]
    print getCoinval
    print getCoinval
    return getCoinval


def gettable(LinkGroupID,LinkID):
    c = db.cursor()
    sql = "SELECT TargetTable from links_to_download where LinkGroupID = " + str(LinkGroupID) +  " and LinkID = " + str(LinkID)
    c.execute(sql)
    for (TargetTable) in c:
        TgtTable = "{}".format(TargetTable)
        trtTable = str(TgtTable)
    cltable = clean(trtTable)

    print sql
    print "The target table to load is " + cltable
    return cltable





def insert_into_chartsDB(LinkGroupID,LinkID):
    coinval =  getbtcval(LinkGroupID,LinkID)
    trttable = gettable(LinkGroupID,LinkID)
    print coinval + " " + trttable
    sql = "INSERT INTO " +str(trttable) + " (`cur_Time`, `cur_Value`) VALUES (" +"'"+ (dt) +"'" + ", " +str(coinval) + ")" +';'
    print sql
    try:
        c = db.cursor()
        c.execute(sql)
        db.commit()
        c.close()
        print "Data successfully load to chart DB"
    except:
        print"somthing went wrong"




def etlchartscoins():
    c = db.cursor()
    sql = "SELECT count(*) as cnt from links_to_download"
    print sql
    c.execute(sql)
    countrows = c.fetchone()
    print clean(str(countrows))
    #print clean(countrows)
    #
    #for n in range (0,countrows-1):
    #    insert_into_chartsDB(1,n)
    #    print "Insert from linkID " + n



    #print cntrows


insert_into_chartsDB(1,1)
