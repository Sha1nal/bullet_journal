# Generated by Django 2.1.7 on 2019-03-21 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bj', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes_Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_text', models.TextField()),
                ('date_created', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag_Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bj.Notes_Notes')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_text', models.CharField(max_length=20)),
                ('note_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bj.Notes_Notes')),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_text', models.TextField()),
                ('is_complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='tag_notes',
            name='tag_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bj.Tags'),
        ),
    ]
