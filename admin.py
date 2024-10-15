from flask import Flask,Blueprint,render_template,request,redirect,url_for,session
import uuid

from database import *


admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():
    return render_template('admin_home.html')



@admin.route('/admin_userview',methods=['post','get'])
def admin_userview():
    data={}
    
    c="select * from register"
    data['view']=select(c)
    return render_template('admin_userview.html',data=data)



@admin.route('/admin_addcategory',methods=['get','post'])
def admin_addcategory():
    data={}
    if 'ADD' in request.form:
        catname=request.form['category_name']
        h="insert into category values(null,'%s')"%(catname)
        insert(h)
         
    d="select * from category"
    data['vitem']=select(d)
    
    if 'action' in request.args:
        action=request.args['action']
        cid=request.args['cid']
        
    else:
        action=None
        
    if action=='update':
        p="select * from category"
        data['up']=select(p)
        
    if 'update' in request.form:
         catname=request.form['category_name']
         
         d="update category set category_name='%s' where category_id='%s'"%(catname,cid)
         update(d)
         return redirect(url_for('admin.admin_addcategory'))
                    
    if action=='delete':
        f="delete from category where category_id='%s'"%(cid)
        delete(f)       
        return redirect(url_for('admin.admin_addcategory'))

        
        
    return render_template('admin_addcategory.html',data=data)


@admin.route('/admin_addproduct', methods=['get','post'])
def admin_addproduct():
    data={}
    
    f="select * from category"
    data['cat']=select(f)
    
    if 'submit' in request.form:
        category=request.form['category_id']
        product=request.form['pname']
        details=request.form['details']
        price=request.form['price']
        quantity=request.form['qnty']
        image=request.files['img']
        path="static/image/"+str(uuid.uuid4())+image.filename
        image.save(path)
        b="insert into product (category_id,product_name, details, price, quantity,image) values ('%s','%s', '%s', '%s', '%s','%s')" % (category,product, details, price, quantity,path)
        insert(b)
    
    p = "select * from product inner join category using (category_id)"
    data['vieww'] = select(p)
    
    if 'action' in request.args:
        action=request.args['action']
        pid=request.args['pid']
    else:
        action=None
    
    if action == 'update':
        f="select * from product inner join category using(category_id) where product_id='%s'"%(pid)
        data['dw']=select(f)
    
    if 'update' in request.form:
        category=request.form['category_id']
        product=request.form['pname']
        details=request.form['details']
        price=request.form['price']
        quantity=request.form['qnty']
        image=request.files['img']
        path="static/image/"+str(uuid.uuid4())+image.filename
        image.save(path)
        
        b="update product set category_id='%s',product_name='%s',details='%s',price='%s',quantity='%s',image='%s' where product_id='%s'" %(category,product,details,price,quantity,path,pid)
        update(b)
        return redirect(url_for('admin.admin_addproduct'))
    
    if action=='delete':
        f="delete from product where product_id='%s'"%(pid)
        delete(f)
        return redirect(url_for('admin.admin_addproduct'))

    
    return render_template('admin_addproduct.html',data=data)

@admin.route('/admin_viewcomplaint', methods=['get','post'])
def admin_viewcomplaint():
    data={}
    
    d='select * from complaint'
    data['cvieww']=select(d)
    return render_template('admin_viewcomplaint.html',data=data)


@admin.route('/admin_replay',methods=['get','post'])
def admin_replay():
    
    if 'submit' in request.form:
        comp_id=request.args['comp_id']
        replay=request.form['replay']
        
        v="update complaint set replay='%s' where comp_id='%s'"%(replay,comp_id)
        update(v)    
        return redirect(url_for('admin.admin_viewcomplaint'))

    return render_template('admin_replay.html')

@admin.route('/admin_shopview',methods=['get','post'])
def admin_shopview():
    data={}
    
    f="select * from shop"
    data['svieww']=select(f)
    
    if 'action' in request.args:
        action = request.args['action']
        sid = request.args['sid']
        lid=request.args['lid']
    else:
        action = None
        
    if action=='accept':

        h="update shop set status='accept' where shop_id='%s'"%(sid)
        update(h)
        f="update login set usertype='shop' where login_id='%s'"%(lid)
        update(f)
        return redirect(url_for('admin.admin_shopview'))

        
    if action=='reject':
        f="delete from shop where shop_id='%s'"%(sid)
        delete(f)
        k="delete from login where login_id='%s'"%(lid)
        delete(k)
        return redirect(url_for('admin.admin_shopview'))
    
        
    return render_template('admin_shopview.html',data=data)

        