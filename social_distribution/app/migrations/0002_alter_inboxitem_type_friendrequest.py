# Generated by Django 4.1.2 on 2022-10-27 07:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inboxitem',
            name='type',
            field=models.CharField(choices=[('POST', 'post'), ('COMMENT', 'comment'), ('LIKE', 'like'), ('FRIENDREQUEST', 'friendrequest')], max_length=13),
        ),
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_author', to=settings.AUTH_USER_MODEL)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_target', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
