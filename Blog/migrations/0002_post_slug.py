# Generated by Django 3.0.5 on 2020-05-02 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='kuchbhi', max_length=255),
            preserve_default=False,
        ),
    ]
