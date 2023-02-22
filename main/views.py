from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import Company
from .forms import EmployeeForm

# Create your views here.


def companies_view(request):
    return render(request, 'companies.html', {"companies": Company.objects.all()})


def add_employee(request, company_id):
    company = Company.objects.get(id = company_id)

    # if request is post then get the employee and assign it to the current company
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():

            employee = form.cleaned_data['employee']
            employee.company = company
            employee.save()

            return redirect('/')
    else:
        form = EmployeeForm()

    payload = {'form': form, 'company' : company}

    return render(request, 'add_employee.html', payload)
