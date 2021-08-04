#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import all packages
get_ipython().system('pip install selenium')
from selenium import webdriver
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import pandas as pd
from datetime import datetime
#create list of map links of roads
links=['https://www.google.co.in/maps/dir/433,+Lokmanya+Bal+Gangadhar+Tilak+Rd,+Sadashiv+Peth,+Pune,+Maharashtra+411030/1021,+Lokmanya+Bal+Gangadhar+Tilak+Rd,+Dadawadi,+Shukrawar+Peth,+Pune,+Maharashtra+411042/@18.5065585,73.8470093,15z/am=t/data=!4m13!4m12!1m5!1m1!1s0x3bc2c076792f3a49:0xe74132c925c49259!2m2!1d73.844441!2d18.5116961!1m5!1m1!1s0x3bc2c013e01f72b3:0x2fa0ecd1e12cb9b2!2m2!1d73.8581769!2d18.5011932?hl=en&authuser=2','https://www.google.co.in/maps/dir/Fergusson+College+Rd,+Deccan+Gymkhana,+Pune,+Maharashtra/Fergusson+College+Rd,+Rage+Path,+Shivajinagar,+Pune,+Maharashtra/@18.524201,73.8338902,15z/am=t/data=!4m13!4m12!1m5!1m1!1s0x3bc2c07f4daa097f:0xce339b60765d5009!2m2!1d73.8416177!2d18.5173257!1m5!1m1!1s0x3bc2c07f4daa097f:0xce339b60765d5009!2m2!1d73.8436372!2d18.5297392?hl=en&authuser=2','https://www.google.co.in/maps/dir/18.5128902,73.8438943/RB+Kumthekar+Rd,+Sadashiv+Peth,+Pune,+Maharashtra+411030/@18.5131083,73.8377483,15z/am=t/data=!3m1!4b1!4m14!4m13!1m5!3m4!1m2!1d73.8448693!2d18.5128875!3s0x3bc2c076674212d7:0x31a6fcbd022c6783!1m5!1m1!1s0x3bc2c0716b558837:0xc91a9a889c7b7f34!2m2!1d73.849069!2d18.5133318!3e0?hl=en&authuser=2','https://www.google.co.in/maps/dir/18.5406037,73.8304658/18.5203427,73.8304487/@18.5305349,73.8221619,15z/am=t/data=!3m1!4b1!4m2!4m1!3e0?hl=en&authuser=2','https://www.google.co.in/maps/dir/SBM+Toilet,+Aundh,+Ganeshkhind+Rd,+Sadhu+Vasvani+Nagar,+Aundh,+Pune,+Maharashtra+411007/1153,+Ganeshkhind+Rd,+Rage+Path,+Model+Colony,+Shivajinagar,+Pune,+Maharashtra+411016/@18.5459335,73.7948654,13z/am=t/data=!4m14!4m13!1m5!1m1!1s0x3bc2bf385a3025fd:0x3b1116fecefd0d4f!2m2!1d73.816321!2d18.5584005!1m5!1m1!1s0x3bc2c0804c2c62d7:0xb19a4efcdcd759a9!2m2!1d73.8439158!2d18.5312705!3e0?hl=en&authuser=2','https://www.google.co.in/maps/dir/Baner+Rd,+Chavan+Nagar,+Pashan,+Pune,+Maharashtra/Baner+-+Mahalunge+Rd,+Ram+Nagar,+Baner,+Pune,+Maharashtra+411045/@18.5605887,73.75018,13z/am=t/data=!4m14!4m13!1m5!1m1!1s0x3bc2bf3cdee0bee3:0x914d3698c401d898!2m2!1d73.7972348!2d18.5549566!1m5!1m1!1s0x3bc2becbf68ad25d:0x8241b2863e8b4a6e!2m2!1d73.7665842!2d18.5687174!3e0?hl=en&authuser=2','https://www.google.co.in/maps/dir/18.5300767,73.8747532/18.5437285,73.8835995/@18.5369025,73.8745322,16z/am=t/data=!3m1!4b1!4m2!4m1!3e0?hl=en&authuser=2','https://www.google.co.in/maps/dir/18.5071955,73.7900731/18.5231798,73.6136825/@18.5280822,73.6331298,12z/am=t/data=!3m1!4b1!4m2!4m1!3e0?hl=en&authuser=2','https://www.google.co.in/maps/dir/Slice+Of+Heaven,+353,+Jawaharlal+Nehru+Rd,+Somwar+Peth,+Pune,+Maharashtra+411011/Jawaharlal+Nehru+Rd,+Market+Yard,+Gultekadi,+Pune,+Maharashtra/@18.505916,73.8516404,14z/am=t/data=!4m14!4m13!1m5!1m1!1s0x3bc2b856b99a0b33:0xd705621e5d445494!2m2!1d73.8674777!2d18.5250989!1m5!1m1!1s0x3bc2c02149c631cd:0x3a1db8602a48ed44!2m2!1d73.8706556!2d18.4870203!3e0?hl=en&authuser=2','https://www.google.co.in/maps/dir/18.6149326,73.7650464/Motilal+Oswal+Financial+Services+Limited,+Flat+No+803,+Bldg+A14,+Cluster+Sunway+Phase+3,+Man+Pune,+Hinjawadi,+Pune,+Maharashtra+411057/@18.6032603,73.7432482,15z/am=t/data=!3m1!4b1!4m9!4m8!1m0!1m5!1m1!1s0x3bc2bb3aaf20d61b:0x89440601d874e8dc!2m2!1d73.7389374!2d18.5914307!3e0?hl=en&authuser=2']
# initialize the data structures we will need
grid={}
timelist=[]
placelist=[]
distancelist=[]
ist=[]
i=1
for link in links:
    browser=webdriver.Chrome()
    browser.get(link)
    #time to load the page- you can change depending on your internet service
    time.sleep(10)
    tm=browser.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[3]/div[1]/h1/span[1]/span[1]').text
    dis=browser.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[3]/div[1]/h1/span[1]/span[2]/span').text
    place=browser.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[3]/div[2]/div/div[2]/h1[1]/span').text
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    ist.append(current_time)
    timelist.append(tm)
    distancelist.append(dis)
    placelist.append(place)
    grid['time']=timelist
    grid['distance']=distancelist
    grid['place']=placelist
    grid['ISTtime']=ist
    print(i,' done')
    i+=1
    browser.close()
# convert to excel
data=pd.DataFrame(grid)
data.to_excel("timegriddata.xlsx")

