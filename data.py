#本文件存储需要的数据
keys = [
    "station_train_code",
    "start_station_name",		
    "end_station_name",			
    "from_station_name",		
    "to_station_name",		
    "start_time",		
    "arrive_time",	
    "lishi",			
    "gr_num",	
    "qt_num",	
    "rw_num",	
    "rz_num",	
    "tz_num",	
    "wz_num",	
    "yw_num",	
    "yz_num",	
    "ze_num",	
    "zy_num",	
    "swz_num"	
]

results = {
    "station_train_code": "车次",
    "start_station_name": "始发站",		
    "end_station_name": "终点站",			
    "from_station_name": "出发站",		
    "to_station_name": "到达站",		
    "start_time": "出发时间",		
    "arrive_time": "到达时间",			
    "lishi": "总历时时间",			
    "gr_num": "高级软卧",	
    "qt_num": "其他",	
    "rw_num": "软卧",	
    "rz_num": "软座",	
    "tz_num": "特等座",	
    "wz_num": "无座",	
    "yw_num": "硬卧",	
    "yz_num": "硬座",	
    "ze_num": "二等座",	
    "zy_num": "一等座",	
    "swz_num": "商务座"	
    }

purpose_codes = {
    "成人":"ADULT",
    "学生":"0X00"
    }

station_names_url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js"
