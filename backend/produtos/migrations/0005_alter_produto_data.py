# Generated by Django 4.1 on 2022-08-19 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_alter_produto_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='data',
            field=models.DateField(auto_now=True),
        ),
    ]
