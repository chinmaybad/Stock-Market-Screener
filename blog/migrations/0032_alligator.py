# Generated by Django 2.1.5 on 2019-03-19 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_accumulation_distribution_atr_bands_swing_index_true_range'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alligator',
            fields=[
                ('indicator_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.Indicator')),
                ('interval', models.CharField(default='minute', max_length=100)),
                ('jaw_period', models.CharField(default='13', max_length=100)),
                ('jaw_offset', models.CharField(default='8', max_length=100)),
                ('teeth_period', models.CharField(default='8', max_length=100)),
                ('teeth_offset', models.CharField(default='5', max_length=100)),
                ('lips_period', models.CharField(default='5', max_length=100)),
                ('lips_offset', models.CharField(default='3', max_length=100)),
                ('alligator_field', models.CharField(default='Jaw', max_length=100)),
            ],
            bases=('blog.indicator',),
        ),
    ]
