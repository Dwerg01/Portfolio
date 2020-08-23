# Generated by Django 3.1 on 2020-08-23 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField()),
                ('body', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
