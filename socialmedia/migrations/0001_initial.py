# Generated by Django 5.0 on 2023-12-28 11:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50, verbose_name='FAQ Question')),
                ('answer', models.CharField(max_length=350, verbose_name='FAQ Answer')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='FAQ Creation Timestamp')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Last FAQ Update Timestamp')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Post Description')),
                ('image', models.ImageField(max_length=500, upload_to='Post', verbose_name='Image')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Creation Timestamp')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Last Updated Timestamp')),
                ('post_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liking_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Liking User')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='socialmedia.post', verbose_name='Liked Post')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='Comment Content')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Comment Creation Timestamp')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Last Comment Update Timestamp')),
                ('Commenting_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Commenting User')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='socialmedia.post', verbose_name='Related Post')),
            ],
        ),
    ]