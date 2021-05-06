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
    if request.method=="POST":
        username=request.form['u_name']
        userage=request.form['u_age']
        usermail=request.form['u_email']
        userphno=request.form['u_phno']
        useraddress=request.form['u_address']
        cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO userprofile VALUES(%s,%s,%s,%s,%s)',(usermail,username,userage,userphno,useraddress))
        cursor.connection.commit()
        return redirect(url_for('symptoms'))
    return render_template('profile.html')
    

   

@app.route('/symptoms',methods=['POST','GET'])
def symptoms():
     if request.method=="POST":
        usermail=request.form['u_mail']
        userphno=request.form['u_phno']
        fever=request.form['fever']
        bodypain=request.form['bodypain']
        lowappetite=request.form['lowappetite']
        musclepain=request.form['musclepain']
        cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO usersymptoms VALUES(%s,%s,%s,%s,%s,%s)',(usermail,userphno,fever,bodypain,lowappetite,musclepain,))
        cursor.connection.commit()
        return redirect(url_for('index'))
     return render_template('symptoms.html')

@app.route('/search',methods=['POST','GET']) 
def search():
    if request.method=='POST':
         id=request.form['u_search']
         cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
         cursor.execute('SELECT * FROM results WHERE mail=%s ',(id,))
         docdata=cursor.fetchall()
         
         cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
         cursor.execute('SELECT mail,phno,status FROM results')
         cursor.connection.commit()
         reportdata=cursor.fetchall()
    return render_template('reports.html',reportdata=reportdata,docdata=docdata)
   
    

@app.route('/reports')
def reports():
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT mail,phno,status FROM results')
    cursor.connection.commit()
    reportdata=cursor.fetchall()
    return render_template('reports.html',reportdata=reportdata)   




    


if __name__=='__main__':
    app.debug=True
    app.run()