# Generated by Django 3.2.8 on 2021-10-12 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stackqs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.TextField(blank=True, max_length=255, null=True)),
                ('accepted', models.BooleanField(blank=True, null=True)),
                ('answers', models.SmallIntegerField(blank=True, null=True)),
                ('body', models.TextField(blank=True, max_length=255, null=True)),
                ('closed', models.BooleanField(blank=True, null=True)),
                ('migrated', models.BooleanField(blank=True, null=True)),
                ('notice', models.BooleanField(blank=True, null=True)),
                ('nottagged', models.TextField(blank=True, max_length=255, null=True)),
                ('tagged', models.TextField(blank=True, max_length=255, null=True)),
                ('title', models.TextField(blank=True, max_length=255, null=True)),
                ('userId', models.SmallIntegerField(blank=True, null=True)),
                ('url', models.URLField(blank=True, max_length=255, null=True)),
                ('views', models.SmallIntegerField(blank=True, null=True)),
                ('wiki', models.BooleanField(blank=True, null=True)),
                ('sort', models.TextField(default='activity', max_length=16)),
                ('order', models.TextField(default='desc', max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Stackql',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.TextField(max_length=255)),
                ('owner', models.TextField(max_length=255)),
                ('is_answered', models.BooleanField(blank=True, null=True)),
                ('view_count', models.SmallIntegerField(blank=True, null=True)),
                ('answer_count', models.SmallIntegerField(blank=True, null=True)),
                ('score', models.SmallIntegerField(blank=True, null=True)),
                ('last_activity_date', models.IntegerField(blank=True, null=True)),
                ('creation_date', models.IntegerField(blank=True, null=True)),
                ('last_edit_date', models.IntegerField(blank=True, null=True)),
                ('question_id', models.SmallIntegerField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('question_query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stackq.stackqs')),
            ],
        ),
    ]
