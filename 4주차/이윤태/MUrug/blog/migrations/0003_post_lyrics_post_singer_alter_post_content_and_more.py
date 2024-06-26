# Generated by Django 4.2.11 on 2024-04-03 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lyrics',
            field=models.TextField(default='', verbose_name='노래 가사'),
        ),
        migrations.AddField(
            model_name='post',
            name='singer',
            field=models.CharField(default='', max_length=20, verbose_name='가수 이름'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='노래 평가'),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='post', verbose_name='썸네일 이미지'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='노래 제목'),
        ),
    ]
