"""
URL configuration for dynamic_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web_app.views import *
from admin_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home),
    path('about/', about),
    path('contact/', contact),
    path('shop/', shop),
    path('single-post/', single_post),
    path('single-product/<int:pid>', single_product),
    path('blog/', blog),
    path('del_cart/<int:cid>', del_dart_pro),
    path('cart/', cart_page),
    path('checkout/<str:arr>', check_out),

    # admin pages
    path('register/', register),
    path('admin_home/',admin_login),
    path('logout/',logout),

    # slider management pages of function
    path('dashboard/',dashboard),
    path('slider_management/',slider_admin),
    path('add_slider/',add_slider),
    path('del_slider/<int:del_id>',del_slider),
    path('upd_slider/<int:upd>',upd_slider),

    # category management pages or function
    path('categories/',categories_management),
    path('add_categories/',add_category),
    path('upd_cate/<int:up_id>',upd_cate),
    path('del_cate/<int:dl_id>',del_cate),

    # subcategory management pages of function
    path('subcate/',subcate_management),
    path('add_subcate/',add_subcate),
    path('del_subcate/<int:dl_id>',del_subcate),
    path('upd_subcate/<int:up_id>',upd_subcate),

    # Bills management page of function
    path('bills/',bills),
    path('del_bill/<int:did>',del_bill),
    path('cart_management/',cart_management),
    
    # petacategory management page of function
    path('petacate/',petacate_management),
    path('add_petacate/<int:c_id>',add_petacate),
    path('del_petacate/<int:dl_id>',del_petacate),
    path('upd_petacate/<int:c_id>/<int:up_id>',upd_petacate),

    # product managemnet pags of function
    path('add_product/<int:cid>/<int:sid>/<int:pid>',add_product),
    path('products/',product_management),
    path('upd_product/<int:pid>',upd_product),
    path('del_product/<int:pid>',del_product),

    # user management pages or function
    path('user_management/',user_management),
    # path('upd_user/<int:uid>',upd_user),
    path('del_user/<int:uid>',del_user),

    # website user login
    path('user_login/',user_login),
    path('user_register/',user_reg),
    path('web_logout/',web_logout),

    # Default admin page
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
