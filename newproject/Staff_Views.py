from django.shortcuts import render, redirect
from newapp.models import Staff,Subject,Session_Year,Student,Attendance,Att_Report

def HOME(request):
    return render(request,'Staff/home.html')
def STAFF_TAKE_ATTENDANCE(request):
    staff_id = Staff.objects.get(admin = request.user.id)

    subject = Subject.objects.filter(staff= staff_id)
    session_year = Session_Year.objects.all()

    action = request.GET.get('action')

    get_subject = None
    get_session_year = None
    students = None
    if action is not None:
        if request.method == "POST":
            subject_id=request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = Session_Year.objects.get(id=session_year_id)

            subject = Subject.objects.filter(id=subject_id)
            for i in subject:
                student_id=i.course.id
                students=Student.objects.filter(course_id = student_id)
    context={
        'subject':subject,
        'session_year':session_year,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'action':action,
        'students':students


    }
    return render(request,'Staff/take_attendance.html',context)


def STAFF_SAVE_ATTENDANCE(request):
    if request.method == "POST":
        subject_id= request.POST.get('subject_id')
        session_year_id =request.POST.get('session_year_id')
        attendance_date=request.POST.get('attendance_date')
        student_id = request.POST.getlist('student_id')
        
        get_subject = Subject.objects.get(id=subject_id)
        get_session_year = Session_Year.objects.get(id=session_year_id)
        
        attendance = Attendance(
            subject_id=get_subject,
            attendance_date=attendance_date,
            session_year_id = get_session_year
        )
        attendance.save()  
    return None    