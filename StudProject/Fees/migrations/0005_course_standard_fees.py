# Generated by Django 4.1.3 on 2022-11-17 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fees', '0004_rename_fees_alloted_admissions_fees_allotted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='standard_Fees',
            field=models.FloatField(null=True),
        ),
    ]
