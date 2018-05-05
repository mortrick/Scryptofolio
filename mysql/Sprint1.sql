/*
Tables to hold Crypto current values for charts

*/


create table charts_btc_10min ( 
cur_Time timestamp,
cur_Value float
);


create table charts_bcc_10min ( 
cur_Time timestamp,
cur_Value float
);


create table charts_eth_10min ( 
cur_Time timestamp,
cur_Value float
);

/*
Table to hold link from differnt sources
*/
drop table links_to_download;
create table links_to_download (
SourceID int,
SourceName varchar (100),
LinkID int,
LinkName varchar(30),
LinkGroupID int,
Link varchar (3000)
);

INSERT INTO `charts`.`links_to_download`
(`SourceID`,
`SourceName`,
`LinkID`,
`LinkName`,
`LinkGroupID`,
`Link`)
VALUES
(1,'Quandle',1,'BTC',1,'https://api.cryptowat.ch/markets/bitfinex/btcusd/price');



SELECT Link FROM charts.links_to_download WHERE LinkGroupID = 1 AND LinkID = 1

select * from links_to_download;
