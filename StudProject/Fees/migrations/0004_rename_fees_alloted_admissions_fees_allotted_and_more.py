# Generated by Django 4.1.3 on 2022-11-17 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Fees', '0003_alter_course_course_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admissions',
            old_name='fees_alloted',
            new_name='fees_allotted',
        ),
        migrations.RemoveField(
            model_name='admissions',
            name='fees_altered',
        ),
    ]
