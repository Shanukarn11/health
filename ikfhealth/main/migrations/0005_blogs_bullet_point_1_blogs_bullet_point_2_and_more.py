# Generated by Django 4.0.5 on 2022-08-06 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_description_blogs_description_para1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='bullet_point_1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='bullet_point_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='bullet_point_3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='bullet_point_4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='tag1',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='tag2',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='tag3',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]