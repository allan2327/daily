from flask import (Flask, request, render_template, flash, session, jsonify, abort)
from model import *
from gen_server_func import parse_day, parse_month, parse_year
#for creating days in a given month
from datetime import timedelta, datetime


def is_month(month, year, user_id):
    """ Query Month and Year established in DB
        Returns True or False 
    """
    
    if Day.query.filter_by(month=month, year=year, user_id=user_id).first():
        
        return True


def create_days_month(month, year):
    """ Create and Return array of string days in a given month
        ['dd-mm-yyyy', etc ... ]
    """
    
    day = timedelta(days=1)
    d = datetime(int(year), int(month), 1)
    dates = []

    while d.month == int(month):
        dates.append(d.strftime('%d-%m-%Y'))
        d += day
    
    print("dates, dates, dates, dates", dates)
    return dates

def parse_weekday(date):
    """ Take in date '%d-%m-%Y'
        Return integer representing day of week 0-6
    """
    print ("date", date, type(date))
    return datetime.strptime(date, '%d-%m-%Y').strftime('%w')

def establish_month(month, year, user_id):
    """ Create Blank New Month if Month not in DB
        Returns None
    """
    dates = create_days_month(month, year)

    print dates

    for date in dates:

        day = parse_day(date)
        month = parse_month(date)
        year = parse_year(date)
        weekday = parse_weekday(date)

        row = Day(user_id=user_id, weekday=weekday,day=day, month=month, year=year, adj1="", adj2="", adj3="", colorset_id=1)
        db.session.add(row)
        db.session.commit()


def gather_all_month_content(month, year, user_id):
    """ Return all information form a particular Month """
    
    # return Day.query.filter_by(user_id=user_id, month=month, year=year).order_by(Day.day).all()
    #d.weekday, d.day, d.month, d.year, d.adj1, d.adj2, d.adj3, d.colorset_id, c.user, c.emotion, c.colorHex, c.colorName
    # sql = db.session.execute("SELECT * FROM days AS d JOIN colorsets AS c ON d.user_id=user_id OR c.user=user_id OR c.user= Null").fetchall()
    # db.session.commit()

    # sql = db.session.query(Day, Colorset).filter(Day.user_id == Colorset.basic || Day.user).filter(Day.user_id == user_id).order_by(Day.day).all()

    print ("SQL gather_all_month_content", Day.query.order_by(Day.day).all())

    return Day.query.order_by(Day.day).all()

    
    # return sql

# "colorHex": "#hex", "colorEmot": "emotion", "colorName": "color",
#"colorHex": "#hex","colorEmot": "emotion","colorName": "color",

def format_date_string(obj):
    """ Take in a db tup of Day and Colorset obj form Day/Colorset Join table 
        Return date string "dd-mm-yyyy"
    """

    return str(obj.day) + "-" + str(obj.month) + "-" + str(obj.year) 

def format_date_content_dict(obj):
    """ Take in a db obj from Day table
        Return day content dict  {"adj1": "adj", "adj2": "adj", "adj3": "adj", "colorIdd" : "id"}
    """
    content = {}
    content["adj1"] = obj.adj1
    content["adj2"] = obj.adj2
    content["adj3"] = obj.adj3
    content["weekeday"] = obj.weekday
    content["colorId"] = obj.colorset_id

    print ("content from format_date_content_dict", content)
    return content

def format_dayContent(month, year, user_id):
    """ Return formated month content in state formated
        {"day-month-year": {"adj1": "adj", "adj2": "adj", "adj3": "adj",  "colorset_id" : "id"}, etc..}
    """
    dayContent = {}

    days_array = gather_all_month_content(month, year, user_id)

    for obj in days_array:
        date_string = format_date_string(obj)
        dayContent[date_string] = format_date_content_dict(obj)



    return dayContent
