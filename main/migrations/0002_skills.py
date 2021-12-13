# Generated by Django 3.2.4 on 2021-12-13 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(upload_to='skills')),
                ('percentage', models.IntegerField(blank=True, null=True)),
                ('is_keyskill', models.BooleanField(default=False)),
            ],
        ),
    ]