# Generated by Django 4.0.2 on 2022-04-27 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_workstatus_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='packing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255)),
                ('quantity', models.CharField(max_length=255)),
            ],
        ),
    ]
