# Generated by Django 4.0.5 on 2022-08-08 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_blogs_bullet_point_1_blogs_bullet_point_2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(db_index=True, primary_key=True, serialize=False)),
                ('keydata', models.CharField(db_index=True, max_length=200, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('shortDescription', models.TextField(blank=True, null=True)),
            ],
        ),
    ]