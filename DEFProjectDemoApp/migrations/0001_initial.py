# Generated by Django 5.1.2 on 2024-10-30 05:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CountryName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DeptName', models.CharField(max_length=50)),
                ('LocationName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('TitleName', models.CharField(max_length=30)),
                ('HasPassport', models.BooleanField()),
                ('Salary', models.IntegerField()),
                ('HireDate', models.DateField()),
                ('Notes', models.CharField(max_length=200)),
                ('Email', models.EmailField(default='', max_length=50)),
                ('PhoneNumber', models.IntegerField()),
                ('Country', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Countries', to='DEFProjectDemoApp.country')),
                ('Department', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Departments', to='DEFProjectDemoApp.department')),
            ],
        ),
    ]
