# Generated by Django 3.1.7 on 2021-03-29 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polling', '0010_auto_20210329_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creatpoll',
            name='o1',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='creatpoll',
            name='o2',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='creatpoll',
            name='o3',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='creatpoll',
            name='o4',
            field=models.TextField(),
        ),
    ]
