# Generated by Django 2.1.7 on 2020-11-18 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oj', '0015_auto_20201118_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='difficulty',
            field=models.CharField(choices=[(0, '简单'), (1, ' 中等'), (2, '困难')], default=0, max_length=40, verbose_name='选项一'),
        ),
    ]
