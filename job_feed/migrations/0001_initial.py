# Generated by Django 4.0.5 on 2022-06-24 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=1000)),
                ('fulldescription', models.TextField(max_length=1000)),
                ('work', models.TextField(max_length=1000)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('sector', models.TextField(max_length=1000)),
                ('experience', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]