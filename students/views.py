from django.shortcuts import get_object_or_404, redirect, render
from .models import Student
from django.db.models import Q
from django.core.paginator import Paginator


def student_list(request):
    search = request.GET.get("search", "")

    students = Student.objects.all()

    if search:
       students = students.filter(
            Q(name__icontains=search) |
            Q(email__icontains=search) |
            Q(course__icontains=search)
        )

    paginator = Paginator(students, 10)
    page_number = request.GET.get("page")

    students = paginator.get_page(page_number)

    return render(request, "students/student_list.html", {"students":students,"search":search} )





def student_create(request):
    
    if request.method == "POST":

        Student.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            course=request.POST.get("course"),
            semester=request.POST.get("semester"),
        )

        return redirect("student_list")

    return render(
        request,
        "students/student_form.html"
    )


def student_update(request,id):
    student = get_object_or_404(Student,id=id)
    if request.method == "POST":
        student.name =request.POST.get("name")
        student.email =request.POST.get("email")
        student.phone =request.POST.get("phone")
        student.course =request.POST.get("course")
        student.semester =request.POST.get("semester")
        student.save()
        return redirect("student_list")

    return render(request,"students/student_form.html",{"student": student})


def student_delete(request,id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.delete()
        return redirect("student_list")

    return render(request, "students/student_confirm_delete.html",{"student":student})