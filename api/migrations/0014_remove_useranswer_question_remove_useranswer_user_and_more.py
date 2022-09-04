# Generated by Django 4.1 on 2022-09-04 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_rename_questions_question_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useranswer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='bringing_child',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='party_count',
            field=models.IntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='UserAnswer',
        ),
    ]