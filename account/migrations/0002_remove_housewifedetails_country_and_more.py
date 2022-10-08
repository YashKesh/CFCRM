# Generated by Django 4.0.3 on 2022-10-08 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionaldetails',
            name='prop_owner',
            field=models.BooleanField(
                choices=[(None, 'Select Yes Or No'), (True, 'Yes'), (False, 'No')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='leads',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]