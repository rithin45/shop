from flask import Flask,Blueprint,render_template,request,redirect,url_for,session

from database import *


public=Blueprint('public',__name__)



@public.route('/')
def home():
    return render_template('index.html')

@public.route('/login',methods=['post','get'])
def login():
    if 'submit' in request.form:
        username=request.form['username']
        password=request.form['password']
        
        h="select * from login where user_name='%s' and password='%s'"%(username,password)
        res=select(h)
        session['lid']=res[0]['login_id']
          
        if res:
        
            if res[0]['usertype']=='admin':
                return redirect(url_for('admin.admin_home'))
            
            elif res[0]['usertype']=='user':
                h="select * from register where login_id='%s'"%(session['lid'])
                res2=select(h)
                if res2:
                    session['uid']=res2[0]['user_id']
                    return redirect(url_for('user.user_home'))
                
            elif res[0]['usertype']=='pending':
                b="select * from shop where login_id='%s'"%(session['lid'])
                res3=select(b)
                if res3:
                    session['sid']=res3[0]['shop_id']
                    return redirect(url_for('shop.shop_home'))
            
        else:
            
            return "username/password is wrong!"
        
    return render_template('login.html')

@public.route('/user_register',methods=['post','get'])
def user_register():
    if 'register' in request.form:
        first_name=request.form['fname']
        last_name=request.form['lname']
        house_name=request.form['hname']
        place=request.form['place']
        land_mark=request.form['lmark']
        pincode=request.form['pcode']
        phone_number=request.form['pnumber']
        email=request.form['email']
        username=request.form['username']
        password=request.form['password']
        
        j="insert into login values(null,'%s','%s','user')"%(username,password)
        res=insert(j)
        
        k="insert into register values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(res,first_name,last_name,house_name,place,land_mark,pincode,phone_number,email)
        insert(k)
    
    return render_template('user_register.html')

@public.route('/shop_register',methods=['get','post'])
def shop_register():
    if 'submit' in request.form:
        shopname=request.form['sname']
        place=request.form['splace']
        landmark=request.form['lmark']
        phone=request.form['sphone']
        email=request.form['mail']
        username=request.form['username']
        password=request.form['password']
        
        j="insert into login values(null,'%s','%s','pending')"%(username,password)
        res=insert(j)
        h="insert into shop values(null,'%s','%s','%s','%s','%s','%s','pending')"%(res,shopname,place,landmark,phone,email)
        insert(h)
        
    return render_template('shop_register.html')