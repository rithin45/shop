from flask import Flask,Blueprint,render_template,request,session,url_for,redirect

from database import *

user=Blueprint('user',__name__)

@user.route('/user_home')
def user_home():
    return render_template('user_home.html')


@user.route('/user_viewproducts')
def user_viewproducts():
    data={}
    r='select * from product'
    data['prod']=select(r)
    return render_template('user_viewproducts.html',data=data)

@user.route('/user_complaint',methods=['get','post'])
def user_complaint():
    data={}
    d='select * from complaint'
    data['cview']=select(d)
    
    if 'submit' in request.form:
        complaint=request.form['complaint']
        p="insert into complaint values(null,'%s','%s','pending',curdate())"%(session['uid'],complaint)     #curdate() used for getting current date
        insert(p)
        return redirect(url_for('user.user_complaint'))
    return render_template('user_complaint.html',data=data)