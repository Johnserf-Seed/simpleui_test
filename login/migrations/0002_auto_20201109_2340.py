# Generated by Django 2.1.7 on 2020-11-09 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=256, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_number',
            field=models.CharField(max_length=128, unique=True, verbose_name='学号'),
        ),
    ]
