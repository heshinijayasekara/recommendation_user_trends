
#implement flask
import requests
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
#
# app = Flask(__name__)
# api = Api(app)
#
# @app.route('/')
# def index():
#     return "test my first flask"
#
# if __name__=='__main__':
#     app.run(debug=True)





# #get data from REST API
# import requests
# response = requests.get("https://randomuser.me/api/")
# # print(response.text)
# x = response.json()
# # print((x.keys()))
# df = pd.DataFrame(x['results'])
# df.to_csv('hesh.csv')
# # print(df.head())
# # x.keys().This
# # will
# # yield ['count', '_links', 'teams']
