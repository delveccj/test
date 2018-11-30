# Generated by Django 2.1.1 on 2018-11-16 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nefarious', '0003_auto_20181112_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='TorrentBlacklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='watchmovie',
            name='transmission_torrent_hash',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='watchtvepisode',
            name='transmission_torrent_hash',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]