# Generated by Django 2.2.11 on 2022-07-06 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0297_auto_20220619_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bed',
            name='bed_type',
            field=models.IntegerField(choices=[(1, 'ISOLATION'), (2, 'ICU'), (6, 'BED_WITH_OXYGEN_SUPPORT'), (7, 'REGULAR')], default=7),
        ),
    ]
