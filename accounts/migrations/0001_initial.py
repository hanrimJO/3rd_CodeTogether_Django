# Generated by Django 3.0.5 on 2020-04-15 22:19

import accounts.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('type', models.BooleanField(default=False)),
                ('social', models.BooleanField(default=False)),
                ('valid', models.BooleanField(default=False)),
                ('naver_email', models.EmailField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'members',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('member_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='subject_teacher', serialize=False, to='accounts.Member')),
                ('image', models.ImageField(upload_to=accounts.models.teacher_path)),
                ('introduce', models.TextField(blank=True)),
            ],
        ),
    ]
