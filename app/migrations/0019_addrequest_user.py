# Generated by Django 4.0.2 on 2022-04-28 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_rename_contact_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='addrequest',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.register'),
        ),
    ]
