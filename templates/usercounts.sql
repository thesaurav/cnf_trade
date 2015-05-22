delete from resp_fact where feed_date = '{{ rdate.start }}';
delete from search_fact where feed_date = '{{ rdate.start }}';
delete from report_user_counts where rpt_date = '{{ rdate.start }}';
/* USER SQL
*/
insert into report_user_counts (rpt_date, hb_unique) SELECT DATE(feed_date), count(distinct uid) as total from feedparser_heartbeat where feed_date between '{{ rdate.start }}' and '{{ rdate.end }}' group by DATE(feed_date);
update report_user_counts, (SELECT count(*) as total from feedparser_heartbeat where feed_date between '{{ rdate.start }}' and '{{ rdate.end }}') as sf set hb_total = sf.total where rpt_date = '{{ rdate.start }}';
update report_user_counts, (SELECT count(distinct user) as total from feedparser_search_feed where feed_date between '{{ rdate.start }}' and '{{ rdate.end }}') as sf set logins = sf.total where rpt_date = '{{ rdate.start }}';
/*
 SAERCH_FACT ROLLER 
*/
insert into search_fact (user,userid,type,subtype,category,subcategory,keyword,city,area,imei,cbsname,cellid,mcc,mnc,lac,lat,lng,page,distance,mode,plid,rg_state,rg_city,rg_district,feed_date,total) select user,userid,type,subtype,category,subcategory,keyword,city,area,imei,cbsname,cellid,mcc,mnc,lac,lat,lng,page,distance,mode,plid,rg_state,rg_city,rg_district, DATE(feed_date),count(*) from feedparser_search_feed where feed_date between '{{ rdate.start }}' and '{{ rdate.end }}' group by DATE(feed_date),user,userid,type,subtype,category,subcategory,keyword,city,area,imei,cbsname,cellid,mcc,mnc,lac,lat,lng,page,distance,mode,plid,rg_state,rg_city,rg_district;
/*
 RESP_FACT ROLLER 
*/
insert into resp_fact (user,userid,type,subtype,pois,offers_global,offers_local,feed_date,mode,total) select user,userid,type,subtype,SUM(pois),SUM(offers_global),SUM(offers_local),DATE(feed_date),mode,COUNT(*) from feedparser_resp_feed where feed_date between '{{ rdate.start }}' and '{{ rdate.end }}' group by DATE(feed_date),user,userid,type,subtype,mode;
