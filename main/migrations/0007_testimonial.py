# Generated by Django 3.2.4 on 2021-12-13 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default='images/user-img.jpg', null=True, upload_to='portfolio')),
            ],
        ),
    ]
