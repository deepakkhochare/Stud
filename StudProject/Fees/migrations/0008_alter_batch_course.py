# Generated by Django 4.1.3 on 2022-11-17 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fees', '0007_batch_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='course',
            field=models.CharField(choices=[('Java Developer', 'Java Developer'), ('Python Full Stack Developer', 'Python Full Stack Developer')], max_length=80, null=True),
        ),
    ]