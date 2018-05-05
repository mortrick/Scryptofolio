# This fuction receive data from web API and store it in the DB
import urllib
import MySQLdb
import datetime

# Define Time

db = MySQLdb.connect("localhost","bot","bobo123","charts")
dt = datetime.datetime.now()
dt = str(dt)[0:16]
print dt
# url = "https://api.cryptowat.ch/markets/bitfinex/btcusd/price"




# Input Group , linkID
# Output link
def getlinks(LinkGroupID,LinkID):
    c = db.cursor()
    sql = "SELECT Link FROM charts.links_to_download WHERE LinkGroupID = " +str(LinkGroupID) + " AND LinkID = " + str(LinkID)
    print sql
    c.execute(sql);
    for (Link) in c:
        Link = "{}".format(Link)
        Link = Link.replace("'","").replace("(","").replace(")","").replace(",","")
        c.close()
        print Link
    return str(Link)


#Input Link
#Output Coin value
def getbtcval(LinkGroupID,LinkID):
    response = urllib.urlopen(getlinks(LinkGroupID,LinkID))
    bitjson = response.read()
    getbtcval = bitjson[19:23]
    print bitjson
    print getbtcval
    return getbtcval


def insert_into_chartsDB(LinkGroupID,LinkID):
    bitval =  getbtcval(LinkGroupID,LinkID)
    print bitval
    sql = "INSERT INTO charts_btc_10min (cur_Time, cur_Value) VALUES (" +"'"+ dt+"'" + "," + str(bitval) + ")"
    print sql
    c = db.cursor()
    c.execute(sql)
    c.close()


insert_into_chartsDB(1,1);



#getbtcval(1,1)
