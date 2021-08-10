from django.shortcuts import render,redirect
from owner import forms
from django.contrib import messages
from .models import Mobile
# Create your views here.
def brand_create(request):
    form=forms.BrandCreationForm()
    context={"form":form}
    if request.POST:
        form=forms.BrandCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Brand has been created")
            return redirect("addbrands")
        else:
            messages.error(request,"brand creation failed")
            return redirect("addbrands")
    return render(request,"brand_create.html",context)

def mobile_create(request):
    context={}
    form=forms.MobileCreationForm()
    context["form"]=form
    if request.method=="POST":
        form=forms.MobileCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Mobile has been created")
            return redirect("addmobiles")
        else:
            messages.error(request, "brand creation failed")
            context["form"]=form
            return render(request,"mobile_create.html",context)
    return render(request,"mobile_create.html",context)
def list_mobile(request):
    mobiles=Mobile.objects.all()
    context={"mobiles":mobiles}
    return render(request,"list_mobiles.html",context)
def mobile_update(request,id):
    mobile=Mobile.objects.get(id=id)
    form=forms.MobileUpdationForm(instance=mobile)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=forms.MobileUpdationForm(data=request.POST,files=request.FILES,instance=mobile)
        if form.is_valid():
            form.save()
            return redirect("mobilelist")
        else:
            return render(request,"mobile_edit.html",context)
    return render(request,"mobile_edit.html",context)
def mobile_detail(request,id):
    mobile=Mobile.objects.get(id=id)
    context={"mobile":mobile}
    return render(request,"mobile_detail.html",context)
def mobile_delete(request,id):
    mobile=Mobile.objects.get(id=id)
    mobile.delete()
    return redirect("mobilelist")
# def brand_search(request):
#     brand=Brand.objects.all()
#     context={}
#     context["brand"]=brand
#     form=BrandSearchForm()
#     context["form"]=form
#     if request.method=="POST":
#         form=BrandSearchForm(request.POST)
#         if form.is_valid():
#             brand_name=Brand.objects.filter(brand_name__contains=brand_name)
#             print(brand)
#             context["brand"]=brand
#             return render(request,"brand_list.html",context)
#         else:
#             context["form"]=form
#             return render(request,"brand_list.html",context)
#     return render(request,"brand_list.html",context)
#