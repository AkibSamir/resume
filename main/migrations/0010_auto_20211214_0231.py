# Generated by Django 3.2.4 on 2021-12-13 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cv',
            field=models.FileField(blank=True, help_text='Download CV', null=True, upload_to='cv'),
        ),
    ]