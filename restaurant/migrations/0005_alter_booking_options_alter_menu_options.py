# Generated by Django 4.2.7 on 2023-11-13 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_alter_booking_id_alter_menu_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'Booking', 'verbose_name_plural': 'Booking Records'},
        ),
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': 'Menu', 'verbose_name_plural': 'Menu Items'},
        ),
    ]
