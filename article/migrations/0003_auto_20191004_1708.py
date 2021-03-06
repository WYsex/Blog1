# Generated by Django 2.2.1 on 2019-10-04 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20191004_1659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author',
            new_name='art_author',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='click',
            new_name='art_click',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='content',
            new_name='art_content',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='date',
            new_name='art_date',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='des',
            new_name='art_des',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='picture',
            new_name='art_picture',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='recommend',
            new_name='art_recommend',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='title',
            new_name='art_title',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='tp',
            new_name='art_tp',
        ),
        migrations.AddField(
            model_name='article',
            name='art_status',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
