#username : admin password: 12345
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views,Hod_Views,Staff_Views,Student_Views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name = 'base'),
    # login path
    path('',views.LOGIN,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='logout'),
    
    path('profile',views.PROFILE,name='profile'),
    path('profile/update',views.PROFILE_UPDATE,name='profile_update'),

    # hod panel
    path('Hod/Home',Hod_Views.HOME,name='hod_home'),
    path('Hod/Student/Add',Hod_Views.ADD_STUDENT,name='add_student'),
    path('Hod/Student/View',Hod_Views.VIEW_STUDENT,name='view_student'),
    path('Hod/Student/Edit/<str:id>',Hod_Views.EDIT_STUDENT,name='edit_student'),
    path('Hod/Student/Update',Hod_Views.UPDATE_STUDENT,name='update_student'),
    path('Hod/Student/Delete/<str:admin>',Hod_Views.DELETE_STUDENT,name='delete_student'),
    
    path('Hod/Staff/Add',Hod_Views.ADD_STAFF,name='add_staff'),
    path('Hod/Staff/View',Hod_Views.VIEW_STAFF,name='view_staff'),
    path('Hod/Staff/Delete/<str:admin>',Hod_Views.DELETE_STAFF,name='delete_staff'),


    
    path('Hod/Course/Add',Hod_Views.ADD_COURSE,name='add_course'),
    path('Hod/Course/View',Hod_Views.VIEW_COURSE,name='view_course'),
    path('Hod/Course/Edit/<str:id>',Hod_Views.EDIT_COURSE,name='edit_course'),
    path('Hod/Course/Update',Hod_Views.UPDATE_COURSE,name='update_course'),
    path('Hod/Course/Delete/<str:id>',Hod_Views.DELETE_COURSE,name='delete_course'),
    
    
    path('Staff/Home',Staff_Views.HOME,name='staff_home'),
    path('Staff/TakeAttendance',Staff_Views.STAFF_TAKE_ATTENDANCE,name='staff_take_attendance'),
    path('Staff/SaveAttendance',Staff_Views.STAFF_SAVE_ATTENDANCE,name='staff_save_attendance'),

    path('Hod/Subject/Add',Hod_Views.ADD_SUBJECT,name='add_subject'),
    path('Hod/Subject/View',Hod_Views.VIEW_SUBJECT,name='view_subject'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
