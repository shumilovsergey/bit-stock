# Generated by Django 5.0.3 on 2024-04-12 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_telegramusers_stoks_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='telegramusers',
            old_name='stoks_id',
            new_name='stocks_id',
        ),
    ]
