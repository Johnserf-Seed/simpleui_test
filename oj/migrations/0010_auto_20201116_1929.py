# Generated by Django 2.1.7 on 2020-11-16 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oj', '0009_auto_20201116_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='author',
            field=models.CharField(max_length=400, verbose_name='作者'),
        ),
    ]