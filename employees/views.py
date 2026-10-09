from django.shortcuts import get_object_or_404, redirect, render
from .models import Employee

def employee_list(request):
    search = request.GET.get("search", "")
    employees = Employee.objects.all()

    if search:
        employees = employees.filter(name__icontains=search)

    return render(
        request,
        "employees/employee_list.html",
        {"employees": employees, "search": search},
    )

def employee_create(request):
    if request.method == "POST":
        Employee.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            department=request.POST.get("department"),
            position=request.POST.get("position"),
            salary=request.POST.get("salary"),
            joining_date=request.POST.get("joining_date"),
        )
        return redirect("employee_list")

    return render(request, "employees/employee_form.html")

def employee_update(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        employee.name = request.POST.get("name")
        employee.email = request.POST.get("email")
        employee.phone = request.POST.get("phone")
        employee.department = request.POST.get("department")
        employee.position = request.POST.get("position")
        employee.salary = request.POST.get("salary")
        employee.joining_date = request.POST.get("joining_date")
        employee.save()
        return redirect("employee_list")

    return render(
        request,
        "employees/employee_form.html",
        {"employee": employee},
    )

def employee_delete(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        employee.delete()
        return redirect("employee_list")

    return render(
        request,
        "employees/employee_confirm_delete.html",
        {"employee": employee},
    )




def employee_list(request):
    employee = Employee.objects.all()

    return render(request,"employees/employee_list.html", {"employee":employee})