# Generated by Django 3.2.3 on 2021-05-23 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cowryRest', '0003_alter_randomuuid_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='randomuuid',
            options={'ordering': ('time',)},
        ),
    ]