# Generated by Django 4.1.2 on 2022-11-23 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_like_comment_alter_like_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='host',
            field=models.TextField(default='http://cmsjmnet'),
        ),
        migrations.AlterField(
            model_name='post',
            name='origin',
            field=models.TextField(default='http://cmsjmnet'),
        ),
        migrations.AlterField(
            model_name='post',
            name='source',
            field=models.TextField(default='http://cmsjmnet'),
        ),
    ]
