from flask import Flask, redirect,render_template
from MySQLdb import connections
from flask import Flask, render_template,send_file,url_for,redirect,flash, request, redirect,session
from flask.wrappers import Response
from flask_mysqldb import MySQL
import MySQLdb.cursors

import os
import io
import re
app=Flask(__name__,template_folder='templates')

app.secret_key="key"
app.secret_key = "super secret key"
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='doccovid'
mysql=MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile',methods=['POST','GET'])
def profile():
    

    return render_template('profile.html')


if __name__=='__main__':
    app.debug=True
    app.run()