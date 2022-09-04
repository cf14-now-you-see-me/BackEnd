# Generated by Django 4.1 on 2022-09-04 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_place_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=256)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.questions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_number', models.IntegerField()),
                ('account_id', models.IntegerField()),
                ('transaction_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('qty', models.IntegerField()),
                ('price_sum', models.IntegerField()),
                ('confirmation', models.CharField(max_length=256, null=True)),
                ('status', models.IntegerField(choices=[(0, 'Waiting'), (1, 'Confirmed'), (2, 'Cancelled')], default=0)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.package')),
            ],
        ),
    ]
