# Generated by Django 2.1.5 on 2019-03-23 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_aroon_awesome_oscillator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ultimate_Oscillator',
            fields=[
                ('indicator_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.Indicator')),
                ('cycle1', models.CharField(default='7', max_length=100)),
                ('cycle2', models.CharField(default='14', max_length=100)),
                ('cycle3', models.CharField(default='28', max_length=100)),
                ('interval', models.CharField(default='minute', max_length=100)),
            ],
            bases=('blog.indicator',),
        ),
        migrations.CreateModel(
            name='Williams',
            fields=[
                ('indicator_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.Indicator')),
                ('period', models.CharField(default='14', max_length=100)),
                ('interval', models.CharField(default='minute', max_length=100)),
            ],
            bases=('blog.indicator',),
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
