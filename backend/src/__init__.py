from flask import Flask
from flask_restx import Resource, Api
# instantiate the app
# app = Flask(__name__)
# api = Api(app)
# class Ping(Resource):
#     def get(self):
#         return {
#             'status': 'success',
#             'message': 'pong!'
#         }
# api.add_resource(Ping, '/ping')

from flask import Flask,request
from flask_cors import CORS
from flask_restx import Resource, Api
# from flask_pymongo import PyMongo
# from pymongo.collection import Collection
import pandas as pd
import json
import numpy as np
from collections import Counter
import csv
# Configure Flask & Flask-PyMongo:
app = Flask(__name__)
# allow access from any frontend
cors = CORS()
cors.init_app(app, resources={r"*": {"origins": "*"}})
# add your mongodb URI
# app.config["MONGO_URI"] = "mongodb://localhost:27017/companiesdatabase"
# pymongo = PyMongo(app)
# Get a reference to the companies collection.
# companies: Collection = pymongo.db.companies
api = Api(app)

#加载全局dataframe，待做
# dataframe=

#加载csv文件
csv_file = "./result.csv"
csv_data = pd.read_csv(csv_file, low_memory = False)#防止弹出警告
csv_df = pd.DataFrame(csv_data)
# print(csv_df.head())
# print(csv_df.info())

#json
geojson_state = json.load(open('./california-counties.geojson','r'))

#为map加载df
df_map_file = "./spatialData.csv"
df_map_data = pd.read_csv(df_map_file, low_memory = False)#防止弹出警告
df_map = pd.DataFrame(df_map_data)
# print(df_map.head())
# print(df_map.info())
us_state_to_abbrev = {

    "Alabama": "AL",

    "Alaska": "AK",

    "Arizona": "AZ",

    "Arkansas": "AR",

    "California": "CA",

    "Colorado": "CO",

    "Connecticut": "CT",

    "Delaware": "DE",

    "Florida": "FL",

    "Georgia": "GA",

    "Hawaii": "HI",

    "Idaho": "ID",

    "Illinois": "IL",

    "Indiana": "IN",

    "Iowa": "IA",

    "Kansas": "KS",

    "Kentucky": "KY",

    "Louisiana": "LA",

    "Maine": "ME",

    "Maryland": "MD",

    "Massachusetts": "MA",

    "Michigan": "MI",

    "Minnesota": "MN",

    "Mississippi": "MS",

    "Missouri": "MO",

    "Montana": "MT",

    "Nebraska": "NE",

    "Nevada": "NV",

    "New Hampshire": "NH",

    "New Jersey": "NJ",

    "New Mexico": "NM",

    "New York": "NY",

    "North Carolina": "NC",

    "North Dakota": "ND",

    "Ohio": "OH",

    "Oklahoma": "OK",

    "Oregon": "OR",

    "Pennsylvania": "PA",

    "Rhode Island": "RI",

    "South Carolina": "SC",

    "South Dakota": "SD",

    "Tennessee": "TN",

    "Texas": "TX",

    "Utah": "UT",

    "Vermont": "VT",

    "Virginia": "VA",

    "Washington": "WA",

    "West Virginia": "WV",

    "Wisconsin": "WI",

    "Wyoming": "WY",

    "District of Columbia": "DC",

    "American Samoa": "AS",

    "Guam": "GU",

    "Northern Mariana Islands": "MP",

    "Puerto Rico": "PR",

    "United States Minor Outlying Islands": "UM",

    "U.S. Virgin Islands": "VI",

}

#test
year=[2016,2017,2018,2019,2020,2021]
month=[1,2,3,4,5,6,7,8,9,10,11,12]
day = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
period = ['Day','Night']
hour = list(range(0,24))
year_list=[122024, 163918, 163176, 258615, 625864, 1511745]
month_list = [198365, 194995, 158224, 171880, 181944, 226561, 159111, 178670, 241822,299131, 360696, 473943]
day_list = [419821, 443968, 455037, 463477, 492074, 311691, 259274]
period_list = [1811935, 1030540]
hour_list = [68800, 59370, 55443, 48656, 51805, 80303, 111160, 135191, 130879, 108779, 103926, 113271, 143715, 166473, 191480, 214264, 218385, 220358, 168982, 116911, 94682, 87078,81188,74243]
merge_year = {'year': year,
                'year_list': year_list}

df_year = pd.DataFrame(merge_year)

merge_month = {
                'month': month,
                'month_list': month_list}

df_month = pd.DataFrame(merge_month)

merge_day = {
                'day': day,
                'day_list': day_list}

df_day= pd.DataFrame(merge_day)

merge_period = {
                'period': period,
                'period_list': period_list}

df_period= pd.DataFrame(merge_period)

merge_hour = {
                'hour': hour,
                'hour_list': hour_list}

df_hour= pd.DataFrame(merge_hour)


#传回json数据的
class YearData(Resource):
    def get(self,args=None):
        orient='split'
        df_json = df_year.to_json(orient=orient, force_ascii=False)
        return json.loads(df_json)
#或者直接传回value
class YearDataValues(Resource):
    def get(self,args=None):
        year=df_year["year"].tolist()
        year_list=df_year["year_list"].tolist()
        returndict={
            "x":year,
            "y":year_list
        }
        return returndict

class MonthData(Resource):
    def get(self,args=None):
        orient='split'
        df_json = df_month.to_json(orient=orient, force_ascii=False)
        return json.loads(df_json)
#或者直接传回value
class MonthDataValues(Resource):
    def get(self,args=None):
        month=df_month["month"].tolist()
        month_list=df_month["month_list"].tolist()
        returndict={
            "x":month,
            "y":month_list
        }
        return returndict

class DayData(Resource):
    def get(self,args=None):
        orient='split'
        df_json = df_day.to_json(orient=orient, force_ascii=False)
        return json.loads(df_json)

class DayDataValues(Resource):
    def get(self,args=None):
        day=df_day["day"].tolist()
        day_list=df_day["day_list"].tolist()
        returndict={
            "x":day,
            "y":day_list
        }
        return returndict

class PeriodData(Resource):
    def get(self,args=None):
        orient='split'
        df_json = df_period.to_json(orient=orient, force_ascii=False)
        return json.loads(df_json)

class PeriodDataValues(Resource):
    def get(self,args=None):
        period=df_period["period"].tolist()
        period_list=df_period["period_list"].tolist()
        returndict={
            "x":period,
            "y":period_list
        }
        return returndict

class HourData(Resource):
    def get(self,args=None):
        orient='split'
        df_json = df_hour.to_json(orient=orient, force_ascii=False)
        return json.loads(df_json)

class HourDataValues(Resource):
    def get(self,args=None):
        hour=df_hour["hour"].tolist()
        hour_list=df_hour["hour_list"].tolist()
        returndict={
            "x":hour,
            "y":hour_list
        }
        return returndict

#Prediction
class PredictionBar(Resource):
    def get(self,args=None):
        #得到参数
        args = request.args.to_dict()
        print(args)
        level = [1, 2, 3, 4]
        level_prob = [0, 0, 0, 0]

        weather=str(args["weather"])
        period = str(args["period"])
        crossing = str(args["crossing"])
        signal = str(args["signal"])
        junction = str(args["junction"])
        # print(weather,period,crossing,signal,junction)
        # weather: 1:fair, 2:fog, 3: rain, 4: snow
        # period:  0:Night 1:Day
        periodmapping={"Night":0,"Day":1}
        weathermapping = {"Fine": 1, "Rainy": 3,"Fog":2,"Snowy":4}

        sunrise_sunset=periodmapping[period]
        Junction=1 if junction=="true" else 0
        Crossing = 1 if crossing == "true" else 0
        Signal = 1 if signal == "true" else 0
        weather=weathermapping[weather]

        for i,row in csv_df.iterrows():
            if int(row["Sunrise_Sunset"])==sunrise_sunset and int(row["Junction"])==Junction and int(row["Crossing"])==Crossing and int(row["Traffic_Signal"])==Signal and int(row["Weather_Condition_Mapped"])==weather:
                level_prob=[row["p_severity_1"],row["p_severity_2"],row["p_severity_3"],row["p_severity_4"]]


        # load model and compute possibilities

        # hour=df_hour["hour"].tolist()
        # hour_list=df_hour["hour_list"].tolist()

        best=level[np.argmax(level_prob)]
        returndict={
            "x":level,
            "y":level_prob,
            "best":best
        }
        return returndict


# class GetStateList(Resource):
#     def get(self,args=None):
#         sl=set(df_map["State"])
#         sl.add("All")
#         sorted(sl)
#         statelist=list(.add("All"))
#         returndict = {
#             "statelist": statelist,
#         }
#         # print("state list length:",len(statelist))
#         return returndict

class GetCountyList(Resource):
    def get(self,args=None):
        args = request.args.to_dict()
        state=args["state"]
        if state=="All":
            countyset=set(df_map["County"].tolist())
            # countyset.add("All")
            countylist=list(countyset)
            countylist.insert(0,"All")
            countylist.sort()
        else:
            state_abb=us_state_to_abbrev[state]
            countyset=set(df_map[df_map["State"]==state_abb]["County"].tolist())
            # countyset.add("All")
            countylist = list(countyset)
            countylist.insert(0, "All")
            countylist.sort()

        print("county list length for state {}:{}".format(state,len(countylist)))
        returndict = {
            "countylist": countylist,
        }
        return returndict


def spatialCount(df_drop, state, county):

    if (state == 'All'):
        if county=="All":
            df = pd.DataFrame(dict(
                x=Counter(df_drop['State']).keys(),
                y=Counter(df_drop['State']).values()
            ))
        else:
            df = pd.DataFrame(dict(
                x=Counter(df_drop[df_drop['County'] == county]['City']).keys(),
                y=Counter(df_drop[df_drop['County'] == county]['City']).values()
            ))
    else:
        if (county == 'All'):
            state = us_state_to_abbrev[state]
            df = pd.DataFrame(dict(
                x=Counter(df_drop[df_drop['State'] == state]['County']).keys(),
                y=Counter(df_drop[df_drop['State'] == state]['County']).values()
            ))
        else:
            df = pd.DataFrame(dict(
                x=Counter(df_drop[df_drop['County'] == county]['City']).keys(),
                y=Counter(df_drop[df_drop['County'] == county]['City']).values()
            ))
    df = df.rename(columns={"y": "Number"})
    return df

class GetSpatialDataBar(Resource):
    def get(self,args=None):
        args = request.args.to_dict()
        state = args["state"]
        county = args["county"]
        print(args)
        return_df=spatialCount(df_map,state,county)
        region=return_df["x"].tolist()
        numberAccident = return_df["Number"].tolist()
        returndict = {
            "region": region,
            "count":numberAccident
        }
        return returndict

class GetSpatialDataMap(Resource):
    def get(self,args=None):
        args = request.args.to_dict()
        state = args["state"]
        county = args["county"]
        print("GetSpatialDataMap:",args)
        if state=="California" and county=="All":
            return_df = spatialCount(df_map, state, county)
            region = return_df["x"].tolist()
            numberAccident = return_df["Number"].tolist()
            returndict = {
                "region": region,
                "count": numberAccident,
                "geojson":geojson_state
            }
            print("return json")
            return returndict
        else:
            return {}


#其他传数据也是大同小异，个人认为不需要用到数据库，照着上面的来就可以

#别忘了加这个
api.add_resource(YearData, '/YearData')
api.add_resource(YearDataValues, '/YearDataValues')
api.add_resource(MonthData, '/MonthData')
api.add_resource(MonthDataValues, '/MonthDataValues')
api.add_resource(DayData, '/DayData')
api.add_resource(DayDataValues, '/DayDataValues')
api.add_resource(PeriodData, '/PeriodData')
api.add_resource(PeriodDataValues, '/PeriodDataValues')
api.add_resource(HourData, '/HourData')
api.add_resource(HourDataValues, '/HourDataValues')

api.add_resource(PredictionBar, '/PredictionBar')
# api.add_resource(GetStateList, '/GetStateList')
api.add_resource(GetCountyList, '/GetCountyList')
api.add_resource(GetSpatialDataBar, '/GetSpatialDataBar')
api.add_resource(GetSpatialDataMap, '/GetSpatialDataMap')
