from django.shortcuts import render, redirect, get_object_or_404

from .models import Student, Group


def student_list(request):
    students = Student.objects.all()

    return render(
        request,
        'student_list.html',
        {'students': students}
    )


def student_detail(request, pk):
    student = get_object_or_404(
        Student,
        id=pk
    )

    return render(
        request,
        'student_detail.html',
        {'student': student}
    )


def student_create(request):
    groups = Group.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        group_id = request.POST.get('group')
        avatar = request.FILES.get('avatar')

        Student.objects.create(
            name=name,
            age=age,
            group_id=group_id,
            avatar=avatar
        )

        return redirect('student_list')

    return render(
        request,
        'student_create.html',
        {'groups': groups}
    )


def student_update(request, pk):
    student = get_object_or_404(
        Student,
        id=pk
    )

    groups = Group.objects.all()

    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.group_id = request.POST.get('group')

        if request.FILES.get('avatar'):
            student.avatar = request.FILES.get('avatar')

        student.save()

        return redirect(
            'student_detail',
            pk=student.id
        )

    return render(
        request,
        'student_update.html',
        {
            'student': student,
            'groups': groups
        }
    )


def student_delete(request, pk):
    student = get_object_or_404(
        Student,
        id=pk
    )

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(
        request,
        'student_delete.html',
        {'student': student}
    )