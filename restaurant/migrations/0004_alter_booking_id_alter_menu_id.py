# Generated by Django 4.2.7 on 2023-11-12 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_booking_id_alter_menu_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]
