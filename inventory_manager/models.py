# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Amovible(models.Model):
    uuid = models.OneToOneField('Objects', models.DO_NOTHING, db_column='uuid', primary_key=True)
    capacity = models.CharField(max_length=36, blank=True, null=True)
    tech = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amovible'

    def __str__(self):
        return '{} {} | {}'.format(self.capacity, self.tech, self.uuid)


class Cable(models.Model):
    uuid = models.OneToOneField('Objects', models.DO_NOTHING, db_column='uuid', primary_key=True)
    length = models.CharField(max_length=36, blank=True, null=True)
    start_type = models.CharField(max_length=36, blank=True, null=True)
    end_type = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cable'

    def __str__(self):
        return '{} | {}/{} | {}'.format(self.length, self.start_type, self.end_type, self.uuid)


class Cpu(models.Model):
    uuid = models.OneToOneField('Objects', models.DO_NOTHING, db_column='uuid', primary_key=True)
    core = models.IntegerField(blank=True, null=True)
    threads = models.IntegerField(blank=True, null=True)
    frequency = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cpu'

    def __str__(self):
        return '{} | {}/{} | {}'.format(self.frequency, self.core, self.threads, self.uuid)

class Drive(models.Model):
    uuid = models.OneToOneField('Objects', models.DO_NOTHING, db_column='uuid', primary_key=True)
    capacity = models.CharField(max_length=36, blank=True, null=True)
    read_value = models.CharField(max_length=36, blank=True, null=True)
    write_value = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drive'

    def __str__(self):
        return '{} | {}/{} | {}'.format(self.capacity, self.read_value, self.write_value, self.uuid)

class Hdd(models.Model):
    uuid = models.OneToOneField(Drive, models.DO_NOTHING, db_column='uuid', primary_key=True)
    rotation_speed = models.CharField(max_length=36, blank=True, null=True)
    size = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hdd'

    def __str__(self):
        return '{} | {} | {}'.format(self.size, self.rotation_speed, self.uuid)


class Historic(models.Model):
    uuid = models.ForeignKey('Objects', models.DO_NOTHING, db_column='uuid')
    date = models.DateTimeField(blank=True, null=True)
    old_status = models.CharField(max_length=36, blank=True, null=True)
    new_status = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historic'


class Objects(models.Model):
    uuid = models.CharField(primary_key=True, max_length=36)
    brand = models.CharField(max_length=36, blank=True, null=True)
    reference = models.CharField(max_length=36, blank=True, null=True)
    serial_number = models.CharField(max_length=36, blank=True, null=True)
    available = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'objects'

    def __str__(self):
        return '{} {} | {}'.format(self.brand, self.reference, "True" if self.available == 1 else "False")

class Ram(models.Model):
    uuid = models.OneToOneField(Objects, models.DO_NOTHING, db_column='uuid', primary_key=True)
    capacity = models.CharField(max_length=36, blank=True, null=True)
    type = models.CharField(max_length=36, blank=True, null=True)
    frequency = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ram'

    def __str__(self):
        return '{} | {}/{} | {}'.format(self.capacity, self.type, self.frequency, self.uuid)

class Smart(models.Model):
    startup_number = models.CharField(max_length=36, blank=True, null=True)
    power_count = models.CharField(max_length=36, blank=True, null=True)
    power_hours = models.CharField(max_length=36, blank=True, null=True)
    health_status = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smart'


class SmartHdd(models.Model):
    id = models.OneToOneField(Smart, models.DO_NOTHING, db_column='id', primary_key=True)
    faulty_sector = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smart_hdd'


class SmartSsd(models.Model):
    id = models.OneToOneField(Smart, models.DO_NOTHING, db_column='id', primary_key=True)
    total_read = models.CharField(max_length=36, blank=True, null=True)
    total_write = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'smart_ssd'


class Ssd(models.Model):
    uuid = models.OneToOneField(Drive, models.DO_NOTHING, db_column='uuid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'ssd'

    def __str__(self):
        return '{}'.format(self.uuid)
