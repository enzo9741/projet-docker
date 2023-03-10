# Generated by Django 4.0.4 on 2022-06-19 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Historic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('old_status', models.CharField(blank=True, max_length=36, null=True)),
                ('new_status', models.CharField(blank=True, max_length=36, null=True)),
            ],
            options={
                'db_table': 'historic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Objects',
            fields=[
                ('uuid', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('brand', models.CharField(blank=True, max_length=36, null=True)),
                ('reference', models.CharField(blank=True, max_length=36, null=True)),
                ('serial_number', models.CharField(blank=True, max_length=36, null=True)),
                ('available', models.IntegerField()),
            ],
            options={
                'db_table': 'objects',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Smart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startup_number', models.CharField(blank=True, max_length=36, null=True)),
                ('power_count', models.CharField(blank=True, max_length=36, null=True)),
                ('power_hours', models.CharField(blank=True, max_length=36, null=True)),
                ('health_status', models.CharField(blank=True, max_length=36, null=True)),
            ],
            options={
                'db_table': 'smart',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Amovible',
            fields=[
                ('uuid', models.OneToOneField(db_column='uuid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='inventory_manager.objects')),
                ('size', models.CharField(blank=True, max_length=36, null=True)),
                ('tech', models.CharField(blank=True, max_length=36, null=True)),
            ],
            options={
                'db_table': 'amovible',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cable',
            fields=[
                ('uuid', models.OneToOneField(db_column='uuid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='inventory_manager.objects')),
                ('length', models.CharField(blank=True, max_length=36, null=True)),
                ('start_type', models.CharField(blank=True, max_length=36, null=True)),
                ('end_type', models.CharField(blank=True, max_length=36, null=True)),
            ],
            options={
                'db_table': 'cable',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cpu',
            fields=[
                ('uuid', models.OneToOneField(db_column='uuid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='inventory_manager.objects')),
                ('core', models.IntegerField(blank=True, null=True)),
                ('threads', models.IntegerField(blank=True, null=True)),
                ('frequency', models.CharField(blank=True, max_length=36, null=True)),
            ],
            options={
                'db_table': 'cpu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Drive',
            fields=[
                ('uuid', models.OneToOneField(db_column='uuid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='inventory_manager.objects')),
                ('capacity', models.CharField(blank=True, max_length=36, null=True)),
                ('read_speed', models.CharField(blank=True, max_length=36, null=True)),
                ('write_speed', models.CharField(blank=True, max_length=36, null=True)),
            ],
            options={
                'db_table': 'drive',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ram',
            fields=[
                ('uuid', models.OneToOneField(db_column='uuid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='inventory_manager.objects')),
                ('capacity', models.CharField(blank=True, max_length=36, null=True)),
                ('type', models.CharField(blank=True, max_length=36, null=True)),
                ('frequency', models.CharField(blank=True, max_length=36, null=True)),
            ],
            options={
                'db_table': 'ram',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SmartHdd',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='inventory_manager.smart')),
                ('faulty_sector', models.CharField(blank=True, max_length=36, null=True)),
            ],
            options={
                'db_table': 'smart_hdd',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SmartSsd',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='inventory_manager.smart')),
                ('total_read', models.CharField(blank=True, max_length=36, null=True)),
                ('total_write', models.CharField(blank=True, max_length=36, null=True)),
            ],
            options={
                'db_table': 'smart_ssd',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hdd',
            fields=[
                ('uuid', models.OneToOneField(db_column='uuid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='inventory_manager.drive')),
                ('rotation_speed', models.CharField(blank=True, max_length=36, null=True)),
            ],
            options={
                'db_table': 'hdd',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ssd',
            fields=[
                ('uuid', models.OneToOneField(db_column='uuid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='inventory_manager.drive')),
            ],
            options={
                'db_table': 'ssd',
                'managed': False,
            },
        ),
    ]
