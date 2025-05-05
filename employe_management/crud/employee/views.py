from django.shortcuts import render,HttpResponseRedirect,redirect
from django.http import HttpResponse
from .forms import employeeform
from .models import employee

# create employee
def create_employee(request):
    if request.method=='POST':
        form=employeeform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form=employeeform()
    return render(request,"create.html",{'form':form})

# list view
def employee_list(request):
    employees=employee.objects.all()
    return render(request,'list.html',{'employees':employees})

# update employee
def employee_update(request,pk):
    emp_obj=employee.objects.get(id=pk)
    if request.method=='POST':
        form=employeeform(request.POST,instance=emp_obj)

        if form.is_valid():
            form.save()
            return redirect('list')
        
    else:
        form=employeeform(instance=emp_obj)
    return render(request,'update.html',{'form':form})

# delete view
def  delete_employee(request,pk):
    emp_obj=employee.objects.get(id=pk)
    if request.method=='POST':
        emp_obj.delete()
        return redirect('list')
    
    return redirect('list')