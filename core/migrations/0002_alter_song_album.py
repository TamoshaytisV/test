# Generated by Django 4.1.6 on 2023-02-07 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='songs', to='core.album'),
        ),
    ]
