from django.urls import path
from . import views
urlpatterns=[
    path('sv/',views.studentView,name="student_url"),
    path('slv/', views.studentlistView, name="studentlist_url"),
    path('suv/<int:pk>/', views.studentupdateView, name="studentupdate_url"),
    path('cv/',views.courseView,name="course_url"),
    path('clv/', views.courselistView, name="courselist_url"),
    path('cuv/<int:pk>/', views.courseupdateView, name="courseupdate_url"),
    path('bv/', views.batchView, name="batch_url"),
    path('blv/', views.batchlistView, name="batchlist_url"),
    path('buv/<int:pk>/', views.batchupdateView, name="batchupdate_url"),
    path('av/', views.admissionView, name="admission_url"),
    path('alv/', views.admissionlistView, name="admissionlist_url"),
    path('auv/<int:pk>/', views.admissionupdateView, name="admissionupdate_url"),
    path('sfee/<str:name>/<str:course>/<str:batch>/<str:fees>/', views.feesView, name="fees_url"),
    path('filter/', views.filterView, name="filter_url"),
    path('export/', views.exportView, name="export_url"),
    path('estud/', views.exportStudent, name="estudent_url"),
    path('ecour/', views.exportCourse, name="ecourse_url"),
    path('ebatch/', views.exportBatch, name="ebatch_url"),
    path('eadmi/', views.exportAdmission, name="eadmission_url"),
    path('', views.home, name="home_url"),
    path('fdv/<str:name>/<str:course>/', views.feesdetailsView, name="feesdetails_url"),
    path('fdel/<str:name>/<str:course>/<str:utr>/', views.feesdeleteView, name="feesdelete_url"),
]