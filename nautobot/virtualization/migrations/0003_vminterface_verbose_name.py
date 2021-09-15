# Generated by Django 3.1.13 on 2021-08-16 13:48

from django.db import migrations
import nautobot.utilities.query_functions


class Migration(migrations.Migration):

    dependencies = [
        ("virtualization", "0002_virtualmachine_local_context_schema"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="vminterface",
            options={
                "ordering": ("virtual_machine", nautobot.utilities.query_functions.CollateAsChar("_name")),
                "verbose_name": "VM interface",
            },
        ),
    ]
