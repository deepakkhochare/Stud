# Generated by Django 4.1.3 on 2022-11-20 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fees', '0011_fees'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fees',
            old_name='batch_name',
            new_name='present_batch_name',
        ),
        migrations.AlterField(
            model_name='fees',
            name='Student_name',
            field=models.CharField(choices=[('Deepak Raghunath Khochare', 'Deepak Raghunath Khochare'), ('Moreshwar Mahadeo Narvekar', 'Moreshwar Mahadeo Narvekar')], default=None, max_length=80, null=True),
        ),
    ]
