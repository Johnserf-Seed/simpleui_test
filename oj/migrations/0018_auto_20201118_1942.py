# Generated by Django 2.1.7 on 2020-11-18 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oj', '0017_auto_20201118_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.CharField(choices=[(0, '简单'), (1, '中等'), (2, '困难')], max_length=40, verbose_name='难度'),
        ),
    ]
