REST API using Flask Framework
Step 1:
     pip install requirements.txt
Step 2:
     Prepare and insert data into MySQL DB using file insertdata.py
Step 3:
     Run restapi.py python file

API can be tested:
	GET http://127.0.0.1:5000/employees (No of database query 1)
	GET http://127.0.0.1:5000/employees?chunk=1 (No of database query 1)
	