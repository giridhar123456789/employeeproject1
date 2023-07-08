from django.shortcuts import render,redirect
from .models import employee
from django.http import HttpResponse
from django.views import View
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class SubmitInput(View):
    def get(self,request):
        return render(request,'employeeinput.html')
class Submit(View):
    def get(self,request):
        e_id=int(request.GET["t1"])
        e_name=request.GET["t2"]
        e_salary=float(request.GET["t3"])
        e_joiningdate=request.GET["t4"]
        e_closingdate=request.GET["t5"]
        e=employee(eid=e_id,ename=e_name,esalary=e_salary,ejoiningdate=e_joiningdate,eclosingdate=e_closingdate)
        e.save()
        return HttpResponse("employee submited successfully")

class Display(View):
    def get(self,request):
        qs=employee.objects.all()
        condic={"records":qs}
        return render(request,'display.html',context=condic)
class DeleteInput(View):
    def get(self,request):
        qs = employee.objects.all()
        condic = {"records": qs}
        return render(request, 'deleteinput.html', context=condic)
class Delete(View):
    def get(self,request):
        e_id=int(request.GET["t1"])
        e=employee.objects.get(eid=e_id)
        e.delete()
        return redirect('/employeeapp/display')
class UpdateInput(View):
    def get(self,request):
        qs = employee.objects.all()
        condic = {"records": qs}
        return render(request, 'updateinput.html', context=condic)
class UpdateDetails(View):
    def get(self,request):
        e_id=int(request.GET["t1"])
        emp=employee.objects.get(eid=e_id)
        condic={'rec':emp}
        return render(request,'update.html',context=condic)
class Update(View):
    def get(self,request):
        e_id=int(request.GET["t1"])
        emp=employee.objects.get(eid=e_id)
        emp.ename=request.GET["t2"]
        emp.esalary=float(request.GET["t3"])
        emp.ejoiningdate=request.GET["t4"]
        emp.eclosingdate=request.GET["t5"]
        emp.save()

        return redirect('/employeeapp/display')