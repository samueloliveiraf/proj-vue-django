# Generated by Django 4.1 on 2022-08-19 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0002_alter_funcionario_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='data',
            field=models.DateField(auto_now=True),
        ),
    ]
