from django.shortcuts import render , redirect
from web_app.models import *
from admin_app.models import *
import random

# Create your views here.n

# custome function
def user_name(uid):
    data = web_user.objects.filter(id=uid)
    user = data.get().username
    return user

# home page
def home(request):

    # obj = obj_slider()
    # print(obj)
    user = ''
    if 'webuid' in request.session:
        user = user_name(request.session['webuid'])

    obj = sliders.objects.all()
    category = categories_data.objects.all()
    pro_obj = product_data.objects.all()

    # for data in  category:
    #     for row in pro_obj:
    #         if data.id == row.category_id:
    #             print(row.name)
    #         # print(row.category_id)

    dp = []
    for row in pro_obj:
        dp.append(row.id)
    random.shuffle(dp)
    disc = []
    for i in range(4):
        disc.append(dp[i])

    dc = random.randint(10,30)

    return render(request,'home.html',{'slider':obj,'category':category,'products':pro_obj,'user':user,'disc':disc,'dc':dc})

def cart_page(request):

    if 'webuid' in request.session:
        user = user_name(request.session['webuid'])
        
    uid = request.session['webuid']
    crt = cart.objects.filter(user_id=uid)
    pro = product_data.objects.all()
    frm = cart_form()

    if 'save' in request.POST:
        cid = request.POST['id']
        data = cart.objects.filter(id=cid).get()
        frm = cart_form(request.POST,instance=data)
        frm.save()
        return redirect('/cart')
    
    if 'checkout' in request.POST:
        pro_id = request.POST
        arr = ''
        for row in pro_id:
            if 'pro_id' in row:
                data = request.POST[row]
                arr = str(data) + '+' + arr

        # check_out(request,pro_list)
        return redirect('/checkout/'+str(arr))
        
    # for data in crt:
    #     for row in pro:
    #         if data.product_id_id == row.id:
    #             print(row.name)

    return render(request,'cart.html',{'cart':crt,'pro':pro,'user':user,'frm':frm,'uid':uid})

def check_out(request,arr):

    pro_ids = []
    total = 0
    for i in arr.split('+'):
        if i != '':
            pro_ids.append(i)

    pro_list = ''
    for row in pro_ids:
        crt = cart.objects.filter(id=row).get()
        am_tot = int(crt.price) * int(crt.qty)
        total += am_tot
        pro_list = pro_list + str(crt.id) + ','

    # total = sum(crt.price)
    print(total)

    ck = checkout_form()

    if 'buy' in request.POST:
        ck = checkout_form(request.POST)
        ck.save()
        return redirect('/')

    return render(request,'checkout.html',{'products':pro_list,'frm':ck,'total':total})
    
def del_dart_pro(request,cid):

    crt = cart.objects.filter(id=cid).get()
    pid = crt.product_id_id
    qty = int(crt.qty)

    pro_data = product_data.objects.filter(id=pid).get()
    pro_qty = int(pro_data.quantity)
    pro_qty = pro_qty + qty
    pro_data.quantity = pro_qty
    pro_data.save()

    cart.objects.filter(id=cid).delete()
    return redirect('/cart')

# user login page
def user_login(request):

    if 'webuid' in request.session:
        web_logout(request)
        return redirect('/')
    msg = ''
    if 'login' in request.POST:
        em = request.POST['em']
        pss = request.POST['pss']
        obj = web_user.objects.filter(email=em,password=pss)
        if obj.count() == 1:
            request.session['webuid'] = obj.get().id
            return redirect('/')
        elif obj.count() != 1:
            msg = 'Email or Password is Incorrect !'
            return render(request,'login.html',{'msg':msg})

    return render(request,'login.html',{'msg':msg})

# user register page
def user_reg(request):

    if 'webuid' in request.session:
        return redirect('/')
    if 'register' in request.POST:
        msg = ''
        em = request.POST['em']
        un = request.POST['un']
        row = web_user.objects.filter(email=em)
        row2 = web_user.objects.filter(username=un)
        row3 = web_user.objects.filter(username=un,email=em)
        if row3.count() >= 1:
            msg = 'Email and username were taken !'
            return render(request,'register.html',{'msg':msg})
        elif row.count() >= 1:
            msg = 'This Email was taken !'
            return render(request,'register.html',{'msg':msg})
        elif row2.count() >= 1:
            msg = 'This Username was taken !'
            return render(request,'register.html',{'msg':msg})
        else:
            a_user = request.POST['un']
            a_email = request.POST['em']
            a_pass = request.POST['pss']

            obj = web_user(
                username = a_user,
                email = a_email,
                password = a_pass
            )
            obj.save()
            return redirect('/user_login')            

    return render(request,'register.html')

# about page
def about(request):
    user = ''
    if 'webuid' in request.session:
        user = user_name(request.session['webuid'])
    return render(request,'about.html',{'user':user})

# contact page 
def contact(request):
    user = ''    
    if 'webuid' in request.session:
        user = user_name(request.session['webuid'])
    return render(request,'contact.html',{'user':user})

# Shop page 
def shop(request):

    category = categories_data.objects.all()
    pro_obj = product_data.objects.all()
    user = ''
    if 'webuid' in request.session:
        user = user_name(request.session['webuid'])

    if 'webuid' not in request.session:
        return redirect('/user_login')
    
    return render(request,'shop.html',{'products':pro_obj,'category':category,'user':user})

# Single post page
def single_post(request):
    if 'webuid' in request.session:
        user = user_name(request.session['webuid'])
    return render(request,'single-post.html',{'user':user})

# Single product page
def single_product(request,pid):

    if 'webuid' in request.session:
        u = web_user.objects.filter(id=request.session['webuid']).get()

    obj = product_data.objects.filter(id=pid).get()
    cate = obj.category.category
    brand = obj.petacate.petacate

    crt = cart.objects.filter(product_id=pid,user_id=u.id)
    if crt.count() > 0:
        return redirect('/cart')

    frm = cart_form()

    if 'add' in request.POST:
        prd = product_data.objects.filter(id=pid).get()
        qty = prd.quantity
        prd.quantity = qty - int(request.POST['qty'])
        prd.save()
        # q = request.POST['qty']
        # print(q)
        frm = cart_form(request.POST)
        frm.save()
        return redirect('/cart')
    

    return render(request,'single-product.html',{'obj':obj,'cate':cate,'brand':brand,'frm':frm,'pro_id':obj.id,'user_id':u.id,'user':u.username})

# def single_product(request,pid):

#     user = ''
#     if 'webuid' not in request.session:
#         return redirect('/user_login')
#     elif 'webuid' in request.session:
#         uid = request.session['webuid']
#         data = web_user.objects.filter(id=uid)
#         user = data.get().username

#     moye = cart_form()

#     if 'add' in request.POST:

#         try:    
#             # if 'qty' in request.POST:
#             #     q = request.POST['qty']
#             #     qty = int(q)
#             #     pro_data = product_data.objects.filter(id=pid).get()
#             #     pro_qty = int(pro_data.quantity)
#             #     pro_qty = pro_qty - qty
#             #     pro_data.quantity = pro_qty
#             #     pro_data.save()

#             moye = cart_form(request.POST)
#             moye.save()
#         except:
#             moye = cart_form(request.POST)
#             moye.save()
#         return redirect('/cart')
    

#     obj = product_data.objects.filter(id=pid).get()
#     tc = obj.category_id
#     c = categories_data.objects.filter(id=tc).get()
#     cate = c.category
#     pc = obj.petacate_id
#     b = petacategories_data.objects.filter(id=pc).get()
#     brand = b.petacate

#     crt = cart.objects.all()
#     for row in crt:
#         if pid == row.product_id_id and uid == row.user_id.id:
#             print(row.user_id.id)
#             print(row.user_id.username)
#             return redirect('/cart')

#     return render(request,'single-product.html',{'obj':obj,'pro_id':pid,'user_id':uid,'user':user,'frm':moye,'cate':cate,'brand':brand})

# Blog page
def blog(request):
    user = ''
    if 'webuid' in request.session:
        user = user_name(request.session['webuid'])
    return render(request,'blog.html',{'user':user})

def web_logout(request):
    del request.session['webuid']       
    # del request.session.items()
    return redirect('/')