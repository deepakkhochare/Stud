from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import StudentForm,CourseForm,admissionForm,batchForm,feesForm
from .models import Students,Course,Batch,Admissions,Fees
import pandas as pd
import numpy
from datetime import date, datetime
from sqlalchemy import create_engine
import xlwt
from django.http import HttpResponse
import mysql.connector

# Create your views here.

def home(request):
    template_name='base.html'
    context={}
    return render(request, template_name, context)

def studentView(request):
    form=StudentForm()
    template_name='Fees/students.html'
    context={'form':form,'msg':"New Student"}
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentlist_url')
        else:
            context = {'form': form, 'msg': "New Student"}
            return render(request, template_name, context)
    my_conn = create_engine("mysql+mysqldb://root:new123@localhost/students")
    conn = my_conn.connect()
    query = "select * from Fees_students"
    my_data = pd.read_sql(query, conn)
    max_count=0
    for i in my_data.index:
        count=my_data['student_id'][i]
        if count>max_count:
            max_count=count
    form.initial['student_id'] = max_count+1
    conn.close()
    return render(request,template_name,context)

def studentlistView(request):
    obj=Students.objects.all()
    template_name='Fees/studentlist.html'
    context={'data':obj}
    return render(request,template_name,context)

def studentupdateView(request, pk):
    obj = Students.objects.get(student_id=pk)
    form = StudentForm(instance=obj)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('studentlist_url')
    template_name = 'Fees/Students.html'
    context = {'form': form,'msg':"Update Student"}
    return render(request, template_name, context)

def courseView(request):
    form=CourseForm()
    template_name='Fees/course.html'
    context={'form':form,'msg':'New Course'}
    if request.method=="POST":
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courselist_url')
    my_conn = create_engine("mysql+mysqldb://root:new123@localhost/students")
    conn = my_conn.connect()
    query = "select * from Fees_course"
    my_data = pd.read_sql(query, conn)
    max_count=0
    for i in my_data.index:
        count=my_data['course_id'][i]
        if count>max_count:
            max_count=count
    form.initial['course_id'] = max_count+1
    conn.close()
    return render(request,template_name,context)

def courselistView(request):
    obj=Course.objects.all()
    template_name='Fees/courselist.html'
    context={'data':obj}
    return render(request,template_name,context)

def courseupdateView(request, pk):
    obj = Course.objects.get(course_id=pk)
    form = CourseForm(instance=obj)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('courselist_url')
    template_name = 'Fees/course.html'
    context = {'form': form,'msg':"Update Course"}
    return render(request, template_name, context)

def batchView(request):
    form=batchForm()
    template_name='Fees/batch.html'
    context={'form':form,'msg':'New Batch'}
    if request.method=='POST':
        form=batchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('batchlist_url')
    my_conn = create_engine("mysql+mysqldb://root:new123@localhost/students")
    conn = my_conn.connect()
    query = "select * from Fees_batch"
    my_data = pd.read_sql(query, conn)
    max_count=0
    for i in my_data.index:
        count=my_data['batch_id'][i]
        if count>max_count:
            max_count=count
    form.initial['batch_id'] = max_count+1
    conn.close()
    return render(request,template_name,context)

def batchlistView(request):
    obj=Batch.objects.all()
    template_name='Fees/batchlist.html'
    context={'data':obj}
    return render(request,template_name,context)

def batchupdateView(request, pk):
    obj = Batch.objects.get(batch_id=pk)
    form = batchForm(instance=obj)
    if request.method == "POST":
        form = batchForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('batchlist_url')
    template_name = 'Fees/batch.html'
    context = {'form': form,'msg':"Update Batch"}
    return render(request, template_name, context)

def admissionView(request):
    form=admissionForm()
    template_name='Fees/admissions.html'
    context={'form':form,'msg':'New Admission'}
    if request.method=='POST':
        form=admissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admission_url')
        else:
            print(form.errors)
    return render(request,template_name,context)

def admissionlistView(request):
    obj=Admissions.objects.all()
    template_name='Fees/admissionlist.html'
    context={'data':obj,'msg':'Admission Details'}
    return render(request,template_name,context)

def admissionupdateView(request, pk):
    obj = Admissions.objects.get(id=pk)
    form = admissionForm(instance=obj)
    if request.method == "POST":
        form = admissionForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('admissionlist_url')
    template_name = 'Fees/admissions.html'
    context = {'form': form,'msg':"Update Admission"}
    return render(request, template_name, context)

def feesView(request,name,course,batch,fees):
    global balance_fees
    form=feesForm()
    template_name='Fees/fees.html'
    context={'form':form,'msg':'Fees Received Entry'}
    if request.method=='POST':
        form=feesForm(request.POST)
        if form.is_valid():
            balance=int(balance_fees)
            entered=int(request.POST.get('amount'))
            if entered>balance:
                msg='Entered amount is greater than balance amount Rs.'+str(balance)
                context = {'form': form, 'msg': msg}
                return render(request, template_name, context)
            else:
                form.save()
                query="select sum(amount) sum from Fees_fees where student_name='" + name + "' and course='" + course + "'"
                my_conn = create_engine("mysql+mysqldb://root:new123@localhost/students")
                conn = my_conn.connect()
                my_data = pd.read_sql(query, conn)
                for ind in my_data.index:
                    sum=my_data['sum'][ind]
                query="update fees_admissions set fees_received=" + str(sum) + " where student_name='" + name + "' and course='" + course + "'"
                conn.execute(query)
                query="update fees_admissions set fees_balance=fees_allotted-fees_received where student_name='" + name + "' and course='" + course + "'"
                conn.execute(query)

                conn.close()
                return redirect('admissionlist_url')

    balance_fees=fees
    form.initial['student_name']=name
    form.initial['course']=course
    form.initial['present_batch_name']=batch
    form.initial['amount']=fees

    my_conn = create_engine("mysql+mysqldb://root:new123@localhost/students")
    conn = my_conn.connect()
    query = "select * from Fees_fees"
    my_data = pd.read_sql(query, conn)
    max_count=0
    for i in my_data.index:
        count=my_data['id'][i]
        if count>max_count:
            max_count=count
    form.initial['id'] = max_count+1
    conn.close()
    return render(request,template_name,context)

def filterView(request):
    if (request.method=="POST"):
        name=request.POST.get('myname')
        name=name.upper()
        obj = Admissions.objects.filter(student_name__contains=name)
        template_name='Fees/admissionlist.html'
        context={'data':obj,'msg':'Filtered Admission List'}
        return render(request,template_name,context)
    template_name='Fees/filter.html'
    context={'msg':'Enter Name to Filter Admissions'}
    return render(request,template_name,context)

def exportView(request):
    template_name='Fees/export.html'
    context={'msg':'Export Data in Excel format'}
    return render(request,template_name,context)

def exportStudent(request):
    my_conn = create_engine("mysql+mysqldb://root:new123@localhost/students")
    cnx = mysql.connector.connect(user='root', password='new123', database='students')
    cursor = cnx.cursor()
    query = "select * from Fees_students"
    cursor.execute(query)
    data = cursor.fetchall()
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="student.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Student_Id', 'Student_Name', 'Email', 'Mobile','Mode',]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column
    font_style = xlwt.XFStyle()
    for row in data:
        row_num += 1
        for col_num in range(len(row)):
            # if type(row[col_num]) is date:
            #     #x=str(date(row[col_num].year,row[col_num].month,row[col_num].day))
            #     x=row[col_num].strftime("%d/%m/%Y")
            #     ws.write(row_num, col_num, x, font_style)
            # else:

            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    cursor.close()
    cnx.close()
    return response

def exportCourse(request):
    my_conn = create_engine("mysql+mysqldb://root:new123@localhost/students")
    cnx = mysql.connector.connect(user='root', password='new123', database='students')
    cursor = cnx.cursor()
    query = "select course_id,course,standard_fees from Fees_course"
    cursor.execute(query)
    data = cursor.fetchall()
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="course.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Course_Id', 'Course', 'Standard Fees',]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column
    font_style = xlwt.XFStyle()
    for row in data:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    cursor.close()
    cnx.close()
    return response

def exportBatch(request):
    my_conn = create_engine("mysql+mysqldb://root:new123@localhost/students")
    cnx = mysql.connector.connect(user='root', password='new123', database='students')
    cursor = cnx.cursor()
    query = "select * from Fees_batch"
    cursor.execute(query)
    data = cursor.fetchall()
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="batch.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Batch_Id', 'Course', 'Batch Name','From Date','Upto Date']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column
    font_style = xlwt.XFStyle()
    for row in data:
        row_num += 1
        for col_num in range(len(row)):
            if type(row[col_num]) is date:
                #x=str(date(row[col_num].year,row[col_num].month,row[col_num].day))
                x=row[col_num].strftime("%d/%m/%Y")
                ws.write(row_num, col_num, x, font_style)
            else:
                ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    cursor.close()
    cnx.close()
    return response

def exportAdmission(request):
    my_conn = create_engine("mysql+mysqldb://root:new123@localhost/students")
    cnx = mysql.connector.connect(user='root', password='new123', database='students')
    cursor = cnx.cursor()
    query = "select * from Fees_admissions"
    cursor.execute(query)
    data = cursor.fetchall()
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="admissions.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Id', 'Student_name', 'Course','Standard_Fees','Fees_Allotted','Fees_Received','Fees_Balance','Original_Batch','Present Batch',]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column
    font_style = xlwt.XFStyle()
    for row in data:
        row_num += 1
        for col_num in range(len(row)):
            if type(row[col_num]) is date:
                #x=str(date(row[col_num].year,row[col_num].month,row[col_num].day))
                x=row[col_num].strftime("%d/%m/%Y")
                ws.write(row_num, col_num, x, font_style)
            else:
                ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    cursor.close()
    cnx.close()
    return response

def feesdetailsView(request,name,course):
    cnx = mysql.connector.connect(user='root', password='new123', database='students')
    cursor = cnx.cursor()
    query = "select fees_allotted,fees_received,fees_balance from Fees_admissions where student_name='" + name + "' and course='" + course + "'"
    cursor.execute(query)
    data = cursor.fetchall()
    print("Data : ",data)
    fees=0
    received=0
    balance=0
    for x in data:
        fees=x[0]
        received=x[1]
        balance=x[2]
    obj = Fees.objects.filter(student_name__contains=name,course__contains=course)
    template_name='Fees/feesdetails.html'
    context={'data':obj,'msg':'Fees Details','fees':fees,'received':received,'balance':balance}
    return render(request,template_name,context)

def feesdeleteView(request,name,course,utr):
    context={'name':name,'course':course,'utr':utr}
    template_name='Fees/deleteconfirm.html'
    if request.method=="POST":
        cnx = mysql.connector.connect(user='root', password='new123', database='students')
        cursor = cnx.cursor()
        query = "delete from Fees_fees where student_name='" + name + "' and course='" + course + "' and UTR_UPI_No='" + utr + "'"
        cursor.execute(query)
        cnx.commit()
        query = "select sum(amount) from Fees_fees where student_name='" + name + "' and course='" + course + "'"
        cursor.execute(query)
        data = cursor.fetchall()
        cnx.commit()
        paid=0
        for x in data:
            paid=x[0]
        print(paid)
        query = "update fees_admissions set fees_received=" + str(paid) + " where student_name='" + name + "' and course='" + course + "'"
        cursor.execute(query)
        cnx.commit()

        query = "update fees_admissions set fees_balance=fees_allotted-fees_received " + " where student_name='" + name + "' and course='" + course + "'"
        cursor.execute(query)
        cnx.commit()

        query = "select fees_allotted,fees_received,fees_balance from Fees_admissions where student_name='" + name + "' and course='" + course + "'"
        cursor.execute(query)
        data = cursor.fetchall()
        print("Data : ",data)
        fees=0
        received=0
        balance=0
        for x in data:
            fees=x[0]
            received=x[1]
            balance=x[2]
        obj = Fees.objects.filter(student_name__contains=name,course__contains=course)
        template_name='Fees/feesdetails.html'
        context={'data':obj,'msg':'Fees Details','fees':fees,'received':received,'balance':balance}
        return render(request,template_name,context)
    return render(request,template_name,context)