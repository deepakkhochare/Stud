# Generated by Django 4.1.3 on 2022-11-17 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fees', '0002_remove_course_batch_no_remove_course_from_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.IntegerField(default=None, max_length=20, null=True),
        ),
    ]
