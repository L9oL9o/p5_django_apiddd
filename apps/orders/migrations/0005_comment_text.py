# Generated by Django 4.1.3 on 2022-11-17 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_blog_educenter_lesson_profile_task_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
