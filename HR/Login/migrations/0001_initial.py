# Generated by Django 3.1.6 on 2021-03-04 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('Experience', models.CharField(max_length=100)),
                ('Current_Company', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Skills', models.TextField(max_length=200)),
                ('CV', models.FileField(upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='Panel_member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Designation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='master_interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Interview_rd', models.IntegerField()),
                ('Job_position', models.CharField(max_length=100)),
                ('Status', models.CharField(max_length=50)),
                ('feedback', models.CharField(max_length=100)),
                ('ispromoted', models.BooleanField()),
                ('Panelmember', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.panel_member')),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.candidate')),
            ],
        ),
    ]
