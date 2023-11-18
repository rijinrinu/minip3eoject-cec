"""realistic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from realisticapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('customer', views.customer, name='customer'),
    path('architect', views.architect, name='architect'),
    path('designer', views.designer, name='designer'),
    path('contractor', views.contractor, name='contractor'),
    path('adminhome', views.adminhome, name='adminhome'),
    path('adminarchitect', views.adminarchitect, name='adminarchitect'),
    path('admindesigner', views.admindesigner, name='admindesigner'),
    path('admincontractor', views.admincontractor, name='admincontractor'),
    path('admincustomer', views.admincustomer, name='admincustomer'),
    path('adminapproveuser', views.adminapproveuser, name='adminapproveuser'),
    path('customerhome', views.customerhome, name='customerhome'),
    path('customerrequirement', views.customerrequirement, name='customerrequirement'),
    path('architecthome', views.architecthome, name='architecthome'),
    path('architectrequest', views.architectrequest, name='architectrequest'),
    path('architectaddplan', views.architectaddplan, name='architectaddplan'),
    path('architectplan', views.architectplan, name='architectplan'),
    path('customerplan', views.customerplan, name='customerplan'),
   # path('customerviewplans', views.customerviewplans, name='customerviewplans'),
    path('customerplanupdate', views.customerplanupdate, name='customerplanupdate'),
    path('customerviewplan', views.customerviewplan, name='customerviewplan'),
    path('customerviewplans', views.customerviewplans, name='customerviewplans'),
    path('customerapprovedplan', views.customerapprovedplan, name='customerapprovedplan'),
    path('customerviewdesigner', views.customerviewdesigner, name='customerviewdesigner'),
    path('customerpassplan', views.customerpassplan, name='customerpassplan'),
    path('customerdesignrequest', views.customerdesignrequest, name='customerdesignrequest'),
    path('customerview3D', views.customerview3D, name='customerview3D'),
    path('customervideo', views.customervideo, name='customervideo'),
    path('customervideoupdate', views.customervideoupdate, name='customervideoupdate'),
    path('customerselectcontractor', views.customerselectcontractor, name='customerselectcontractor'),
    path('customerassignwork', views.customerassignwork, name='customerassignwork'),
    path('customerwork', views.customerwork, name='customerwork'),
    path('designerhome', views.designerhome, name='designerhome'),
    path('designerrequest', views.designerrequest, name='designerrequest'),
    path('designeraddvideo', views.designeraddvideo, name='designeraddvideo'),
    path('contractorhome', views.contractorhome, name='contractorhome'),
    path('contractorrequest', views.contractorrequest, name='contractorrequest'),
    path('assignarchitect', views.assignarchitect, name='assignarchitect'),
    path('showarchitect', views.showarchitect, name='showarchitect'),
    path('contractorapprove', views.contractorapprove, name='contractorapprove'),
    path('addfeedback', views.feedback, name='feedback'),
    path('viewfeedback', views.viewfeedback, name='feedback'),
    path('shop', views.shop, name='shop'),
    path('product', views.product, name='product'),
    path('viewproduct', views.viewproduct, name='viewproduct'),
    path('viewshop', views.adminviewshop, name='adminviewshop'),
    path('shophome', views.shophome, name='shophome'),
    path('viewbooking', views.shopviewbook, name='shopviewbook'),
    path('payment/', views.payment, name='payment'),
    path('payment1/', views.payment1, name='shopviewbook'),
    path('payment2/', views.payment2, name='shopviewbook'),
    path('payment3/', views.payment3, name='shopviewbook'),
    path('payment4/', views.payment4, name='shopviewbook'),
    path('previous', views.previous, name='previous'),
    path('account', views.account, name='account'),
    path('paymentplan', views.paymentplan, name='paymentplan'),
    path('upipayment', views.upipayment, name='upipayment'),
    path('contractorprequest', views.contractorprequest, name='contractorprequest'),
    path('customerpvideo', views.customerpvideo, name='customerpvideo'),
    path('viewaccount', views.viewaccount, name='viewaccount'),
    path('archviewplan', views.archviewplan, name='archviewplan'),
    path('designerviewwork', views.designerviewwork, name='designerviewwork'),
    path('editreq', views.editreq, name='editreq'),
    path('deletecon', views.deletecon, name='deletecon'),
    path('deletearch', views.deletearch, name='deletearch'),
    path('deletedesi', views.deletedesi, name='deletedesi'),
    path('about', views.about, name='about'),
    path('registeration', views.registeration, name='registeration'),
    path('shopview', views.shopview, name='shopview'),
    path('cview', views.cview, name='cview'),





    














    
]
