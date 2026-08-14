from django.shortcuts import render, redirect, get_object_or_404

from .models import Teacher, Group, Student, StudentMark


def home(request):
    students = Student.objects.select_related('group').all().order_by('-created_at')
    context = {
        'teachers_count': Teacher.objects.count(),
        'groups_count': Group.objects.count(),
        'students_count': students.count(),
        'marks_count': StudentMark.objects.count(),
        'students': students,
    }
    return render(request, 'home.html', context)


def teacher_list(request):
    return render(request, 'teacher_list.html', {'teachers': Teacher.objects.all()})


def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)
    groups = teacher.groups.all()
    return render(request, 'teacher_detail.html', {'teacher': teacher, 'groups': groups})


def group_list(request):
    return render(request, 'group_list.html', {'groups': Group.objects.all()})


def group_detail(request, pk):
    group = get_object_or_404(Group, id=pk)
    students = group.students.all()
    return render(request, 'group_detail.html', {'group': group, 'students': students})


def student_list(request):
    students = Student.objects.select_related('group').all().order_by('-created_at')
    return render(request, 'student_list.html', {'students': students})


def student_detail(request, pk):
    student = get_object_or_404(
        Student.objects.select_related('group__mentor'),
        id=pk
    )
    marks = student.marks.select_related('teacher').all().order_by('-created_at')
    return render(request, 'student_detail.html', {'student': student, 'marks': marks})


def student_create(request):
    groups = Group.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        age = request.POST.get('age')
        group_id = request.POST.get('group')
        avatar = request.FILES.get('avatar')

        if name and age and group_id:
            student = Student.objects.create(
                name=name,
                age=age,
                group_id=group_id,
                avatar=avatar
            )
            return redirect('student_detail', pk=student.id)

    return render(request, 'student_create.html', {'groups': groups})


def student_update(request, pk):
    student = get_object_or_404(Student, id=pk)
    groups = Group.objects.all()

    if request.method == 'POST':
        student.name = request.POST.get('name', '').strip()
        student.age = request.POST.get('age')
        student.group_id = request.POST.get('group')

        avatar = request.FILES.get('avatar')
        if avatar:
            student.avatar = avatar

        student.save()
        return redirect('student_detail', pk=student.id)

    return render(request, 'student_update.html', {'student': student, 'groups': groups})


def student_delete(request, pk):
    student = get_object_or_404(Student, id=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'student_delete.html', {'student': student})


def mark_list(request):
    marks = StudentMark.objects.select_related('student__group', 'teacher').all().order_by('-created_at')
    return render(request, 'mark_list.html', {'marks': marks})


def mark_create(request, student_id=None):
    students = Student.objects.select_related('group').all().order_by('name')
    teachers = Teacher.objects.all().order_by('name')
    selected_student = get_object_or_404(Student, id=student_id) if student_id else None

    if request.method == 'POST':
        student_value = request.POST.get('student')
        subject = request.POST.get('subject', '').strip()
        mark_value = request.POST.get('mark')
        teacher_value = request.POST.get('teacher')

        if student_value and subject and mark_value and teacher_value:
            StudentMark.objects.create(
                student_id=student_value,
                teacher_id=teacher_value,
                subject=subject,
                mark=mark_value
            )
            return redirect('student_detail', pk=student_value)

    return render(
        request,
        'mark_create.html',
        {
            'students': students,
            'teachers': teachers,
            'selected_student': selected_student,
        }
    )

def mark_update(request, pk):
    mark = get_object_or_404(StudentMark, id=pk)
    students = Student.objects.select_related('group').all().order_by('name')
    teachers = Teacher.objects.all().order_by('name')

    if request.method == 'POST':
        student_value = request.POST.get('student')
        subject = request.POST.get('subject', '').strip()
        mark_value = request.POST.get('mark')
        teacher_value = request.POST.get('teacher')

        if student_value and subject and mark_value and teacher_value and mark_value.isdigit() and 1 <= int(mark_value) <= 5:
            mark.student_id = student_value
            mark.subject = subject
            mark.teacher_id = teacher_value
            mark.mark = int(mark_value)
            mark.save()
            return redirect('student_detail', pk=mark.student_id)

    return render(
        request,
        'mark_update.html',
        {
            'mark': mark,
            'students': students,
            'teachers': teachers,
        }
    )


def mark_delete(request, pk):
    mark = get_object_or_404(StudentMark, id=pk)
    student_id = mark.student_id

    if request.method == 'POST':
        mark.delete()
        return redirect('student_detail', pk=student_id)

    return render(request, 'mark_delete.html', {'mark': mark})

