# Generated by Django 4.1 on 2024-02-06 15:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "IRWebApp",
            "0004_rename_speech_signature_similarspeeches_speech_similar_1_index_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="similarspeeches",
            old_name="speech_index",
            new_name="speech_id",
        ),
        migrations.RemoveField(
            model_name="similarspeeches",
            name="speech_similar_1_index",
        ),
        migrations.RemoveField(
            model_name="similarspeeches",
            name="speech_similar_2_index",
        ),
        migrations.RemoveField(
            model_name="similarspeeches",
            name="speech_similar_3_index",
        ),
        migrations.AddField(
            model_name="similarspeeches",
            name="speech",
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
