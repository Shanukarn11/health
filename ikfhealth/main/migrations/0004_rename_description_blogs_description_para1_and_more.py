# Generated by Django 4.0.5 on 2022-08-06 15:40

from django.db import migrations, models
import main.storage


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_blogs_pic2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogs',
            old_name='description',
            new_name='description_para1',
        ),
        migrations.AddField(
            model_name='blogs',
            name='description_para2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='description_quote',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogs',
            name='pic1',
            field=models.ImageField(blank=True, null=True, storage=main.storage.OverwriteStorage(), upload_to='courses'),
        ),
    ]