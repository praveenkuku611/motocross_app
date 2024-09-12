from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee



def allemployees(request):
    emp = Employee.objects.all()
    return render(request,"invoicebill_app/allemployees.html",{"allemployees":emp})


def singleemployee(request):
     return render(request,"invoicebill_app/singleemployee.html")

def addemployee(request):
     if request.method == "POST":
          firstname = request.POST['firstName']
          lastname = request.POST['lastName']
          email = request.POST['email']
          phone = request.POST['phone']
          position = request.POST['position']

          e = Employee()
          e.firstname = firstname
          e.lastname = lastname
          e.email = email
          e.phone = phone
          e.position = position
          e.save()
          return redirect("/allemployees")
     return render(request,"invoicebill_app/addemployee.html")



def deleteemployee(request,empid):
     e=Employee.objects.get(pk=empid)
     e.delete()
     return redirect("allemployees")

def updateemployee(request,empid):
     e=Employee.objects.get(pk=empid)
     return render(request,"invoicebill_app/updateemployee.html",{"singleemployee": e})


def doupdateemployee(request,empid):
     # updatedid = request.POST.get('id')
     updatedfirstname = request.POST.get('firstName')
     updatedlastname = request.POST.get('lastName')
     updatedemail = request.POST.get('email')
     updatedphone = request.POST.get('phone')
     updatedposition = request.POST.get('position')

     emp = Employee.objects.get(pk=empid)

     # emp.updatedid = updatedid
     emp.firstname = updatedfirstname
     emp.lastname = updatedlastname
     emp.email = updatedemail
     emp.phone = updatedphone
     emp.position = updatedposition

     emp.save()
     return redirect("allemployees")

