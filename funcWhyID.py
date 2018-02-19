# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 13:58:48 2018

@author: Alex Palomino
"""

def funcWhyID(df1):    
    
    whyIDdict = {'-1' : 'Appropriate skip' ,
    '-7' : 'Refused' ,
    '-8' : 'Dont know' ,
    '-9' : 'Not ascertained' ,
    '1' : 'Home' ,
    '10' : 'Work' ,
    '11' : 'Go to work' ,
    '12' : 'Return to work' ,
    '13' : 'Attend business meeting/trip' ,
    '14' : 'Other work related' ,
    '20' : 'School/religious activity' ,
    '21' : 'Go to school as student' ,
    '22' : 'Go to religious activity' ,
    '23' : 'Go to library: school related' ,
    '24' : 'OS - Day care' ,
    '30' : 'Medical/dental services' ,
    '40' : 'Shopping/errands' ,
    '41' : 'Buy goods: groceries/clothing/hardware store' ,
    '42' : 'Buy services: video rentals/dry cleaner/post office/car service/bank' ,
    '43' : 'Buy gas' ,
    '50' : 'Social/recreational' ,
    '51' : 'Go to gym/exercise/play sports' ,
    '52' : 'Rest or relaxation/vacation' ,
    '53' : 'Visit friends/relatives' ,
    '54' : 'Go out/hang out: entertainment/theater/sports event/go to bar' ,
    '55' : 'Visit public place: historical site/museum/park/library' ,
    '60' : 'Family personal business/obligations' ,
    '61' : 'Use professional services: attorney/accountant' ,
    '62' : 'Attend funeral/wedding' ,
    '63' : 'Use personal services: grooming/haircut/nails' ,
    '64' : 'Pet care: walk the dog/vet visits' ,
    '65' : 'Attend meeting: PTA/home owners association/local government' ,
    '70' : 'Transport someone' ,
    '71' : 'Pick up someone' ,
    '72' : 'Take and wait'}

    df1["whyDesc"] = df1["WHYTO"].map(whyIDdict)