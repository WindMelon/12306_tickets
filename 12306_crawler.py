#! /usr/bin/python
# -*- coding:utf-8 -*-
#author:zhanhao
#Date:2016.12.11
#file:12306_crawler.py

import urllib.request
import json
from data import keys,results,station_names_url,purpose_codes
import re 

def set_station_names(station):
    """
    将输入的中文转化成query_url需要的英文缩写形式，查询不到会弹出IndexError。
    """
    stations = urllib.request.urlopen(station_names_url).read().decode("utf-8")
    station = re.findall(station+"\|(.*?)\|",stations)
    station = station[0]
    return(station)

def print_data(start,end,date,purpose_code):
    """
    提交查询，打印结果
    """
    query = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date="+date+\
    "&leftTicketDTO.from_station="+start+\
    "&leftTicketDTO.to_station="+end+"&purpose_codes="+purpose_codes[purpose_code]
    html = urllib.request.urlopen(query)
    trains = json.loads(html.read().decode("utf-8"))["data"]
    for train in trains:
        for key in keys:
            print(results[key]+":"+train["queryLeftNewDTO"][key],end="\t")
        print("\n")

def start_query():
    """
    初始化查询参数
    """
    while(True):
        try:
            start = set_station_names(input("出发站："))
            break
        except IndexError:
            print("没有此站信息")

    while(True):
        try:
            end = set_station_names(input("到达站："))
            break
        except IndexError:
            print("没有此站信息")
    
    date = input("日期（1970-01-01）:")

    purpose_code = input("成人/学生票:")

    try:
        print_data(start,end,date,purpose_code)
    except KeyError:
        print("没有查询到车次信息！")

if __name__ == "__main__":
    start_query()