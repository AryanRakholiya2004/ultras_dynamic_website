from django.shortcuts import render , redirect
from admin_app.models import *
from web_app.models import *

# Create your views here.

# Login page
def admin_login(request):       

    email = password = ''
    if 'uid' in request.session:
        return redirect('/dashboard')
    else:
        if 'login' in request.POST:
            email = request.POST['em']
            password = request.POST['pss']
            if email == '' or password == '':
                msg = 'Empty Email or Password !'
                return redirect('/admin_home',{'msg':msg})
            obj = user_data.objects.filter(email=email,password=password)
            msg = ''
            if obj.count() == 1:
                row = obj.get()
                request.session['uid'] = row.id
                return redirect('/dashboard')
            else:
                msg = 'Invalid Email or Password !'
                return redirect('/admin_home',{'msg':msg})
    
        return render(request,'index.html')

# Register page
def register(request):

    if 'uid' in request.session:
        return redirect('/dashboard')
    else:
        formobj = userForm()
        if 'register' in request.POST:

            formobj = userForm(request.POST)
            # print(formobj)
            formobj.save()
            return redirect('/admin_home')
    
    return render(request,'register.html',{'frm':formobj})

def dashboard(request):

    user = 'Unknown'
    # if 'uid' in request.session:
    #     uid = request.session['uid']
    #     u = user_data.objects.filter(id=uid).get()
    #     user = u.email
    #     print(user)
    #     print('success')
    if 'uid' not in request.session:
        return redirect('/admin_home')
    else:
        u = user_data.objects.filter(id=request.session['uid']).get()
        user = u.username
        print(user)
        obj = categories_data.objects.all()
        obj2 = subcategories_data.objects.all()
        obj3 = petacategories_data.objects.all()
        pro = product_data.objects.all()
        webuser = web_user.objects.all()
        print(webuser)
        cate_cnt = obj.count()
        sub_cnt = obj2.count()
        peta_cnt = obj3.count()
        pro_cnt = pro.count()
        user_cnt = webuser.count()

    # print(user)
    return render(request,'dashboard.html',{'user':user,'obj':obj,'obj2':obj2,'obj3':obj3,'pro':pro,'webuser':webuser,'cate':cate_cnt,'sub':sub_cnt,'peta':peta_cnt,'pro_cnt':pro_cnt,'usercnt':user_cnt})


def logout(request):
    del request.session['uid']
    return redirect('/admin_home')


def slider_admin(request):

    if 'uid' not in request.session:
        return redirect('/admin_home')
    else:
        # obj = obj_slider()
        obj = sliders.objects.all()

    return render(request,'slider_management.html',{'obj':obj})

def add_slider(request):

    if 'uid' not in request.session:
        return redirect('/admin_home')
    else:

        btn = 'Add Slider'
        objslider = obj_slider()

        if 'add' in request.POST:
            objslider = obj_slider(request.POST,request.FILES)
            objslider.save()
            return redirect('/slider_management')

    return render(request,'add_slider.html',{'frm':objslider,'btn':btn})

def del_slider(request,del_id):

    sliders.objects.filter(id=del_id).delete()

    return redirect('/slider_management')

def upd_slider(request,upd):

    if 'uid' not in request.session:
        return redirect('/admin_home')
    else:
        data = sliders.objects.filter(id=upd).get()
        obj = obj_slider(instance=data)
        
        btn = 'Update Slider'

        if 'add' in request.POST:
            
            obj = obj_slider(request.POST,request.FILES,instance=data)
            obj.save()

            return redirect('/slider_management')

    return render(request,'add_slider.html',{'frm':obj,'btn':btn})



# ======================== Main cate =================================

def categories_management(request):

    if 'uid' not in request.session:
        return redirect('/admin_home')
    obj = categories_data.objects.all()
    return render(request,'categories_management.html',{'obj':obj})

def add_category(request):

    if 'uid' not in request.session:
        return redirect('/admin_home')
    btn = "Add Category"
    # obj = categories_form(request.POST,request.FILES)
    obj = categories_form()
    
    if 'add' in request.POST:
        obj = categories_form(request.POST,request.FILES)
        obj.save()
        return redirect('/categories')

    return render(request,'add_category.html',{'btn':btn,'frm':obj})


def upd_cate(request,up_id):

    if 'uid' not in request.session:
        return redirect('/admin_home')
    btn = "Update Category"
    data = categories_data.objects.filter(id=up_id).get()
    obj = categories_form(instance=data)
    
    if 'add' in request.POST:
        obj = categories_form(request.POST,request.FILES,instance=data)
        obj.save()
        return redirect('/categories')

    return render(request,'add_category.html',{'btn':btn,'frm':obj})


def del_cate(request,dl_id):

    categories_data.objects.filter(id=dl_id).delete()
    return redirect('/categories')


# ======================== Sub cate =================================

def subcate_management(request):
    
    if 'uid' not in request.session:
        return redirect('/admin_home')
    obj = subcategories_data.objects.all()
    return render(request,'subcate_management.html',{'obj':obj})

def add_subcate(request):

    if 'uid' not in request.session:
        return redirect('/admin_home')
    btn = 'Add Subcate'
    obj = categories_data.objects.all()
    # frm = subcate_form(request.POST,request.FILES)
    frm = subcate_form()

    if 'add' in request.POST:
        frm = subcate_form(request.POST,request.FILES)
        frm.save()
        return redirect('/subcate')

    return render(request,'add_subcate.html',{'btn':btn,'obj':obj,'frm':frm})

def del_subcate(request,dl_id):

    subcategories_data.objects.filter(id=dl_id).delete()
    return redirect('/subcate')


def upd_subcate(request,up_id):

    if 'uid' not in request.session:
        return redirect('/admin_home')
    btn = "Update Sub-category"
    data = subcategories_data.objects.filter(id=up_id).get()
    frm = subcate_form(instance=data)
    obj = categories_data.objects.all()
    
    if 'add' in request.POST:
        frm = subcate_form(request.POST,request.FILES,instance=data)
        frm.save()
        return redirect('/subcate')

    return render(request,'add_subcate.html',{'btn':btn,'frm':frm,'obj':obj})



# ======================== peta cate =================================

def add_petacate(request,c_id):
    btn = 'Add Brand'

    if 'uid' not in request.session:
        return redirect('/admin_home')
    obj = subcategories_data.objects.filter(category=c_id)
    # obj2 = categories_data.objects.filter(id=c_id)    
    frm = petacate_form()

    if 'add' in request.POST:

        frm = petacate_form(request.POST,request.FILES)
        frm.save()

        return redirect('/petacate')
    return render(request,'add_petacate.html',{'btn':btn,'obj':obj,'frm':frm,'cat':c_id})

def petacate_management(request):

    if 'uid' not in request.session:
        return redirect('/admin_home')
    obj = petacategories_data.objects.all()
    return render(request,'petacate_management.html',{'obj':obj})

def del_petacate(request,dl_id):

    petacategories_data.objects.filter(id=dl_id).delete()
    return redirect('/petacate')

def upd_petacate(request,c_id,up_id):

    if 'uid' not in request.session:
        return redirect('/admin_home')
    btn = "Update Peta-category"
    data = petacategories_data.objects.filter(id=up_id).get()
    frm = petacate_form(instance=data)
    obj = subcategories_data.objects.filter(category=c_id)

    
    if 'add' in request.POST:
        frm = petacate_form(request.POST,request.FILES,instance=data)
        frm.save()
        return redirect('/petacate')

    return render(request,'add_petacate.html',{'btn':btn,'frm':frm,'obj':obj,'cat':c_id})


# ======================== Product cate =================================

def add_product(request,cid,sid,pid):
    btn = 'Add Product'

    if 'uid' not in request.session:
        return redirect('/admin_home')
    obj = categories_data.objects.filter(id=cid)
    cate = obj.get().category
    # print(cate)
    obj2 = subcategories_data.objects.filter(id=sid)
    sub = obj2.get().subcate
    # print(sub)
    obj3 = petacategories_data.objects.filter(id=pid)
    peta = obj3.get().petacate
    # print(peta)

    frm = product_form()

    if 'add' in request.POST:

        frm = product_form(request.POST,request.FILES)
        frm.save()
        return redirect('/products')

    return render(request,'add_product.html',{'frm':frm,'btn':btn,'p_cate':cate,'p_sub':sub,'p_peta':peta,'cate':cid,'sub':sid,'peta':pid})

def product_management(request):

    if 'uid' not in request.session:
        return redirect('/admin_home')
    obj = product_data.objects.all()
    return render(request,'products_management.html',{'obj':obj})

def upd_product(request,pid):

    if 'uid' not in request.session:
        return redirect('/admin_home')
    btn = "Update Product"
    data = product_data.objects.filter(id=pid).get()
    frm = product_form(instance=data)
    
    if 'add' in request.POST:
        frm = product_form(request.POST,request.FILES,instance=data)
        frm.save()
        return redirect('/products')

    return render(request,'add_product.html',{'btn':btn,'frm':frm})

def del_product(request,pid):
    
    product_data.objects.filter(id=pid).delete()
    return redirect('/products')

# user management 

def user_management(request):

    obj = web_user.objects.all()
    return render(request,'user_management.html',{'obj':obj})

def del_user(request,uid):

    web_user.objects.filter(id=uid).delete()
    return redirect('/user_management')


# bills 
def bills(request):
    obj = checkout.objects.all()
    for row in obj:
        pro_list = []
        for i in row.pro_name.split(','):
            if i != '':
                # print(i)
                pro_crt = cart.objects.filter(id=i).get()
                pro = pro_crt.product_id_id
                pro_det = product_data.objects.filter(id=pro).get()
                pro_list.append(pro_crt)
                # print(pro_crt)
                row.pro_name = []
        # print(pro_list)
        row.pro_name.append(pro_list)
        for pro_det in row.pro_name:
            for row in pro_det:
                print(row)
            print('newline')


    for pro_crt in pro_list:
        print(type(pro_crt))
        print(pro_crt)
    return render(request,'bills_management.html',{'obj':obj,'product':pro_det})

def del_bill(request,did):

    checkout.objects.filter(id=did).delete()
    return redirect('/bills')

def cart_management(request):
    obj = cart.objects.all()
    return render(request,'cart_management.html',{'obj':obj})