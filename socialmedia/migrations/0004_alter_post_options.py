# Generated by Django 5.0 on 2023-12-30 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialmedia', '0003_post_likes_delete_like'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-updated_at']},
        ),
    ]