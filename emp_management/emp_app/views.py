from django.shortcuts import render, HttpResponse
from .models import *
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'index.html')

def all_employee(request):
    all_emp = Employee.objects.all()
    context = {
        'all_emp':all_emp
    }
    return render(request,'all_employee.html', context)

def add_employee(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        department = int(request.POST['department'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = int(request.POST['role'])
        phone_no = int(request.POST['phone_no'])
        hired_date = request.POST['hired_date']
        post_rec = Employee(first_name=first_name,last_name = last_name, address=address, department_id=department, 
                            salary=salary,bonus=bonus, role_id=role, phone_no=phone_no,hired_date=hired_date)
        post_rec.save()
        return HttpResponse('Employee added ')
    elif request.method == 'GET':
        all_emp = Employee.objects.all()
        context = {
        'all_emp':all_emp
    }
        return render(request,'add_employee.html', context)
    else:     
        return render('Exception Ocurred')

def rem_employee(request,emp_id=0):
    if emp_id:
        try:
            emp_removed = Employee.objects.get(id=emp_id)
            emp_removed.delete()
            return HttpResponse('Employee Removed')
        except:
            return HttpResponse('Please Select valid ID')
    all_emp = Employee.objects.all()
    context = {
        'all_emp':all_emp
    }
    return render(request,'rem_employee.html', context)

def filter_employee(request):
    if request.method == 'POST':
        name = request.POST['name']
        department = request.POST['department']
        role = request.POST['role']
        all_emp = Employee.objects.all()
        if name:
            all_emp = all_emp.filter(Q(first_name__icontains=name)|Q(last_name__icontains = name))
        if department:
            all_emp = all_emp.filter(department__name__icontains=department)
        if role:
            all_emp = all_emp.filter(role__role_name__icontains=role)
        
        context = {
            'all_emp': all_emp
        }
        return render(request,'all_employee.html', context)
    elif request.method == 'GET':
        return render(request,'filter_employee.html')
    else:
        return HttpResponse('An Error Ocurred')