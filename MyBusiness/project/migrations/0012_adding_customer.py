# Generated by Django 3.0.4 on 2020-04-16 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='adding',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.Customer'),
        ),
    ]