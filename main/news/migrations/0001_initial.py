# Generated by Django 3.1.1 on 2020-09-24 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('content', models.CharField(max_length=400)),
                ('cate', models.CharField(choices=[('LOC', 'Local'), ('NAT', 'National'), ('INT', 'International')], max_length=3)),
                ('author', models.CharField(choices=[('P1', 'Person 1'), ('P2', 'Person 2'), ('P3', 'Person 3')], max_length=2)),
                ('date', models.DateTimeField()),
                ('img1', models.ImageField(upload_to='')),
                ('img2', models.ImageField(upload_to='')),
            ],
        ),
    ]