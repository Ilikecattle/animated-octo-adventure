# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Car.imageLink'
        db.alter_column(u'caroftheday_car', 'imageLink', self.gf('django.db.models.fields.FilePathField')(path='/home/adam/catharticgames/media', max_length=100))

        # Changing field 'Car.link'
        db.alter_column(u'caroftheday_car', 'link', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):

        # Changing field 'Car.imageLink'
        db.alter_column(u'caroftheday_car', 'imageLink', self.gf('django.db.models.fields.FilePathField')(max_length=100))

        # Changing field 'Car.link'
        db.alter_column(u'caroftheday_car', 'link', self.gf('django.db.models.fields.FilePathField')(max_length=100))

    models = {
        u'caroftheday.car': {
            'Meta': {'object_name': 'Car'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'imageLink': ('django.db.models.fields.FilePathField', [], {'path': "'/home/adam/catharticgames/media'", 'max_length': '100'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'make': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['caroftheday']