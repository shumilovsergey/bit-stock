# Generated by Django 5.0.3 on 2024-04-12 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_telegramusers_stoks_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramusers',
            name='stoks_id',
            field=models.JSONField(default={'active': 'none'}),
        ),
    ]
