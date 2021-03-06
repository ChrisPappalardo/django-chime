# Generated by Django 2.2.6 on 2020-04-10 01:31

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_chime.core
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChimeSite',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(default=None, null=True)),
                ('name', models.CharField(max_length=255)),
                ('population', models.BigIntegerField(default=3600000, help_text='Regional population', validators=[django.core.validators.MinValueValidator(1)])),
                ('current_hospitalized', models.BigIntegerField(default=69, help_text='Currently hospitalized COVID-19 patients', validators=[django.core.validators.MinValueValidator(0)])),
                ('date_first_hospitalized', models.DateField(blank=True, help_text='Date of first hospitalized COVID-19 case, if known', null=True)),
                ('doubling_time', models.FloatField(default=4.0, help_text='Doubling time in days (up to today)', validators=[django.core.validators.MinValueValidator(0.0)])),
                ('hospitalized_days', models.IntegerField(default=7, help_text='Average hospital length of stay (in days)', validators=[django.core.validators.MinValueValidator(0)])),
                ('hospitalized_rate', models.FloatField(default=0.025, help_text='Hospitalization %(total infections)', validators=[django.core.validators.MinValueValidator(1e-05), django.core.validators.MaxValueValidator(1.0)])),
                ('icu_days', models.IntegerField(default=9, help_text='Average days in ICU', validators=[django.core.validators.MinValueValidator(0)])),
                ('icu_rate', models.FloatField(default=0.0075, help_text='ICU %(total infections)', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('infectious_days', models.IntegerField(default=14, help_text='Infectious days', validators=[django.core.validators.MinValueValidator(0)])),
                ('market_share', models.FloatField(default=0.15, help_text='Hospital market share %', validators=[django.core.validators.MinValueValidator(1e-05), django.core.validators.MaxValueValidator(1.0)])),
                ('n_days', models.IntegerField(default=100, help_text='Number of days to project', validators=[django.core.validators.MinValueValidator(0)])),
                ('mitigation_date', models.DateField(blank=True, default=django.utils.timezone.now, help_text='Date social distancing measures went into effect')),
                ('relative_contact_rate', models.FloatField(default=0.3, help_text='Social distancing (% reduction in social contact going forward)', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('ventilated_days', models.IntegerField(default=10, help_text='Average days on ventilator', validators=[django.core.validators.MinValueValidator(0)])),
                ('ventilated_rate', models.FloatField(default=0.005, help_text='Ventilated %(total infections)', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=(django_chime.core.ShortID, models.Model),
        ),
    ]
