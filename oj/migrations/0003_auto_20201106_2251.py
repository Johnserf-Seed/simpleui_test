# Generated by Django 2.1.7 on 2020-11-06 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oj', '0002_auto_20201101_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='right_answer',
            field=models.TextField(blank=True, max_length=40, null=True, verbose_name='正确答案'),
        ),
    ]
