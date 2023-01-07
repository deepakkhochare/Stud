from django import forms
from .models import Students,Course,Admissions,Batch,Fees
from django.core import validators

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields= [
            'student_id',
            'student_name',
            'email',
            'mobile',
            'mode',
            ]
        labels={
            'student_id': 'Student Id',
            'student_name': 'Student Name',
            'email': 'Email Id',
            'mobile': 'Mobile No',
            'mode':'Mode (On/Off)',
            }
        widgets={
            'student_id': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'readonly': 'true'}),
            'student_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'style': 'font-size: 15px',
                    'autocomplete': 'off'}),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off'}),
            'mobile': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off'}),
            # 'mode': forms.TextInput(
            #     attrs={
            #         'class': 'form-control',
            #         'autocomplete': 'off'}),
        }

    def clean_student_name(self):
        sid = self.cleaned_data.get('student_name')
        sid = sid.upper()
        return sid
    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        print(len(mobile))
        if len(mobile)<10 or len(mobile)>10:
            raise validators.ValidationError("Length of Mobile Number should be 10")
        if not mobile.isdigit():
            raise validators.ValidationError("Only numbers are allowed ")
        return mobile

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields= [
            'course_id',
            'course',
            'standard_Fees',
        ]
        labels={
            'course_id': 'course Id',
            'course': 'Course Name',
            'standard_fees': 'Fees',
            }
        widgets={
            'course_id': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'readonly':'true'}),
            'course': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    }),
        }

class admissionForm(forms.ModelForm):
    class Meta:
        model=Admissions
        fields = [
            # 'student_id',
            'student_name',
            # 'course_id',
            'course',
            'present_batch_name',
            'original_batch_name',
            'standard_Fees',
            'fees_allotted',
            'fees_received',
            'fees_balance',
         ]

        labels = {
            # 'student_id':'Student Id',
            'student_name':'Student Name',
            # 'course_id':'Course Id',
            'course':'Course Name',
            'present_batch_name':'Present Batch name',
            'original_batch_name': 'Original Batch name',
            'standard_Fees':'Standard Fees',
            'fees_allotted':'Allotted Fees',
            'fees_received':'Received Fees ',
            'fees_balance':'Balance Fees',
        }
        widgets = {
            'fees_received': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'readonly':'true'}),
            'fees_balance': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'readonly':'true'}),
        }

class batchForm(forms.ModelForm):
    class Meta:
        model=Batch
        fields = [
            'batch_id',
            'course',
            'batch_name',
            'from_date',
            'upto_date',
         ]

        labels = {
            'batch_id':'Batch Id',
            'course': 'Course Name',
            'batch_name':'Batch Name',
            'from_date':'From Date',
            'upto_date':'Upto date',
        }
        widgets = {
            'batch_id': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'readonly':'true'}),
            'course_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',}),
            'from_date': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'type':'date'}),
            'upto_date': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'type':'date'}),
        }

class feesForm(forms.ModelForm):
        class Meta:
            model = Fees
            fields = [
                'id',
                'student_name',
                'course',
                'present_batch_name',
                'payment_date',
                'amount',
                'UTR_UPI_No',
            ]

            labels = {
                'id': 'Id',
                'student_name': 'Student Name',
                'course': 'Course Name',
                'present_batch_name': 'Present Batch Name',
                'payment_date': 'Payment Date',
                'amount': 'Amount Received',
                'UTR_UPI_No': 'UTR_UPI No',
            }
            widgets = {
                'id': forms.TextInput(
                    attrs={
                        'class': 'form-control',
                        'autocomplete': 'off',
                        'readonly':'true'}),
                'course': forms.TextInput(
                    attrs={
                        'class': 'form-control',
                        'autocomplete': 'off', }),
                'present_batch_name': forms.TextInput(
                    attrs={
                        'class': 'form-control',
                        'autocomplete': 'off', }),
                'payment_date': forms.DateInput(
                    attrs={
                        'class': 'form-control',
                        'autocomplete': 'off',
                        'type': 'date'}),

            }


