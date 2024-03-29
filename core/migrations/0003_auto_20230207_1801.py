# Generated by Django 4.1.6 on 2023-02-07 18:01

import json
from pathlib import Path

from django.db import migrations

from mutant.settings import BASE_DIR


def import_data(apps, schema_editor):
    Album = apps.get_model('core', 'Album')
    Song = apps.get_model('core', 'Song')
    with open(Path(BASE_DIR).joinpath('core/fixtures/albums.json'), 'r') as file:
        data = json.load(file)

    for item in data:
        songs = item.pop('songs')
        album = Album.objects.create(**item)
        for song in songs:
            song.update({
                'album': album
            })
            Song.objects.create(**song)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_song_album'),
    ]

    operations = [
        migrations.RunPython(import_data, reverse_code=migrations.RunPython.noop),
    ]
