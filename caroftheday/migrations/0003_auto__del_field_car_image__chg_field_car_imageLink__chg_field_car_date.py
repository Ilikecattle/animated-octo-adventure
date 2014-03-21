# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Car.image'
        db.delete_column(u'caroftheday_car', 'image')


        # Changing field 'Car.imageLink'
        db.alter_column(u'caroftheday_car', 'imageLink', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Car.date'
        db.alter_column(u'caroftheday_car', 'date', self.gf('django.db.models.fields.DateField')())

    def backwards(self, orm):
        # Adding field 'Car.image'
        db.add_column(u'caroftheday_car', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100),
                      keep_default=False)


        # Changing field 'Car.imageLink'
        db.alter_column(u'caroftheday_car', 'imageLink', self.gf('django.db.models.fields.FilePathField')(path='/home/adam/catharticgames/media', max_length=100))

        # Changing field 'Car.date'
        db.alter_column(u'caroftheday_car', 'date', self.gf('django.db.models.fields.DateField')(auto_now=True))

    models = {
        u'caroftheday.car': {
            'Meta': {'object_name': 'Car'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imageLink': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'make': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['caroftheday']