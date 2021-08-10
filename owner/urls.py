from django.urls import path
from owner import views
from django.shortcuts import render
urlpatterns=[
    path('',lambda request:render(request,"base.html")),
    path("mobiles/add",views.mobile_create,name="addmobiles"),
    path("brand/add",views.brand_create,name="addbrands"),
    path("mobiles/",views.list_mobile,name="mobilelist"),
    path("mobiles/change/<int:id>",views.mobile_update,name="mobileedit"),
    path("mobiles/<int:id>",views.mobile_detail,name="mobiledetail"),
    path("mobiles/remove/<int:id>",views.mobile_delete,name="mobiledelete"),
]