from django.shortcuts import render,redirect
from Admin.models import *
# Create your views here.
def district(request):
    district=District.objects.all()
    if request.method == 'POST':
        District.objects.create(name=request.POST.get('district'))
        return render(request,"Admin/District.html")
    else:
        return render(request,"Admin/District.html",{'dis':district})

def districtd(request,did):
    district=District.objects.all()
    District.objects.get(id=did).delete()
    return redirect('webadmin:district')

def category(request):
    return render(request,"Admin/Category.html")
def subcategory(request):
    return render(request,"Admin/Subcategory.html")
def place(request):
    return render(request,"Admin/Place.html")
def adminregister(request):
    adreg=Adminreg.objects.all()
    if request.method=="POST":
        Adminreg.objects.create(name=request.POST.get('aname'),contact=request.POST.get('acontatct'),email=request.POST.get('aemail'),password=request.POST.get('apassword'))
        return render(request,"Admin/AdminRegister.html")
    else:
        return render(request,"Admin/AdminRegister.html",{'a':adreg})

def editdis(request,did):
    editdata=District.objects.get(id=did)
    if request.method=="POST":
        editdata.name=request.POST.get('district')
        editdata.save()
        return redirect('webadmin:district')
    else:
        return render(request,"Admin/District.html",{'edit':editdata})
        