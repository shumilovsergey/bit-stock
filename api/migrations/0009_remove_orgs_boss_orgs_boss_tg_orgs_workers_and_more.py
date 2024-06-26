# Generated by Django 5.0.4 on 2024-04-21 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_orgs_options_orgs_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orgs',
            name='boss',
        ),
        migrations.AddField(
            model_name='orgs',
            name='boss_tg',
            field=models.CharField(default='no-auth', max_length=56),
        ),
        migrations.AddField(
            model_name='orgs',
            name='workers',
            field=models.ManyToManyField(to='api.telegramusers'),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='name',
            field=models.CharField(default='no-name', max_length=56),
        ),
    ]
