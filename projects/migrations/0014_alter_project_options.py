# Generated by Django 3.2.6 on 2021-10-02 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20211002_0837'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total', 'title']},
        ),
    ]