# Generated by Django 3.1.4 on 2020-12-04 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='categories',
            field=models.CharField(choices=[(1, 'Academics'), (2, 'Business'), (3, 'Design'), (4, 'Development'), (5, 'Health & Fitness'), (6, 'IT & Software'), (7, 'language'), (8, 'Lifestyle'), (9, 'Marketing'), (10, 'Music'), (11, 'Officer Productivity'), (12, 'Personal Development'), (13, 'Photography')], max_length=50),
        ),
    ]
