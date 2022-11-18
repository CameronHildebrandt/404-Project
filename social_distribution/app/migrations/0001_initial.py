# Generated by Django 4.1.2 on 2022-11-18 06:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('host', models.TextField(default='http://ohaton')),
                ('url', models.TextField()),
                ('github', models.TextField(blank=True)),
                ('profile_image_url', models.TextField(default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png')),
                ('registered', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('commenter_url', models.TextField()),
                ('comment', models.TextField()),
                ('content_type', models.TextField()),
                ('date_published', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.TextField()),
                ('title', models.TextField()),
                ('date_published', models.DateTimeField(default=django.utils.timezone.now)),
                ('source', models.TextField(default='http://ohaton')),
                ('origin', models.TextField(default='http://ohaton')),
                ('description', models.TextField()),
                ('content_type', models.TextField()),
                ('content', models.TextField()),
                ('categories', models.TextField()),
                ('comments_count', models.IntegerField(default=0)),
                ('comments_url', models.TextField()),
                ('visibility', models.CharField(choices=[('PUBLIC', 'public'), ('PRIVATE', 'private')], max_length=7)),
                ('unlisted', models.BooleanField(default=False)),
                ('author_url', models.TextField()),
                ('received', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('liker_url', models.TextField()),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.post')),
            ],
        ),
        migrations.CreateModel(
            name='InboxItem',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('POST', 'post'), ('COMMENT', 'comment'), ('LIKE', 'like'), ('FOLLOW', 'follow')], max_length=13)),
                ('object_url', models.TextField(null=True)),
                ('from_author_url', models.TextField()),
                ('from_username', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.author')),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('target_url', models.TextField()),
                ('accepted', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.post'),
        ),
    ]
