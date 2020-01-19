# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 14:31:20 2020

@author: omkar
"""
#Libraries to import
import flask
from flask import request
from flask_mysqldb import MySQL
import pandas as pd
from bson.json_util import dumps
from flask import Response
import settings
#Flask app configuration and database setting
app = flask.Flask(__name__)
app.config["DEBUG"] = settings.DEBUG
app.config['MYSQL_HOST'] = settings.MYSQL_HOST
app.config['MYSQL_USER'] = settings.MYSQL_USER
app.config['MYSQL_PASSWORD'] = settings.MYSQL_PASSWORD
app.config['MYSQL_DB'] = settings.MYSQL_DB

#Mysql object
mysql = MySQL(app)

@app.route('/employees', methods=['GET'])
def get_employees():
    """
    Returns a json response of list of employees
    """
    try:
        
        #Intialize mysql connection
        cur = mysql.connection.cursor()
        sql_query = settings.RAW_SQL_QUERY
    
        #Check if chunk query parameter in present and add skip and limit accordingly                  
        chunk = request.args.get('chunk')
        if chunk:
            try:
                skip = (int(chunk) - 1) * 20
                limit = 20
                sql_query = sql_query + f" LIMIT {limit} OFFSET {skip}"
            except Exception as error:
                error = {"error": "chunk should be non-zero positive integer" + " " + str({error})}
                return Response(dumps(error), status=400, mimetype='application/json')
            
        #Execute SQL query    
        cur.execute(sql_query)
        columns = ["RowNumber", "Employee Code", "Department", "Score", "Date Created", "Casetype"]
        employees = pd.DataFrame(list(cur.fetchall()), columns=columns)
        employees = employees.drop(columns=['RowNumber', "Casetype", "Date Created"])
        employees.columns = ['employee_code', "department", "score"]
        employees = employees.to_dict('records')
        cur.close()
        
        #Return response
        response = Response(dumps(employees), status=200, mimetype='application/json')
        
    except Exception as error:
        #Response on error
        response = Response(str(error), status=500)
        
    return response

app.run()