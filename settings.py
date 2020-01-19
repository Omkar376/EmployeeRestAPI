# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 16:58:44 2020

@author: logisticsnowtech5
"""

DEBUG = False

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_DB = 'EmployeeDB'

RAW_SQL_QUERY =  """SELECT floor(@c := @c + 0.25) RowNumber, t.*, 1 Casetype
                    FROM (select @c:= -0.25) initvars, employee t
                    WHERE Department != "Waltzz" and DATE(`Date Created`) < now() - interval 14 DAY
                    union
                    SELECT floor(@n := @n + 0.5) RowNumber, t.*, 2 Casetype
                    FROM (select @n:= -0.5) initvars, employee t
                    WHERE Department = "Waltzz" and DATE(`Date Created`) < now() - interval 14 DAY
                    union
                    SELECT floor(@k := @k + 0.5) RowNumber, t.*,3 Casetype
                    FROM (select @k:= -0.5) initvars, employee t
                    WHERE Department != "Waltzz" and DATE(`Date Created`) >= now() - interval 14 DAY
                    ORDER By RowNumber ASC, Casetype ASC, Score DESC"""
