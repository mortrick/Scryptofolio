LinkGroupID =1
LinkID =2


sql = "SELECT TargetTable from links_to_download where LinkGroupID = " +" "+ str(LinkGroupID) +  "and LinkID = " + str(LinkID);";
print sql
