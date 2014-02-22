# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Car'
        db.create_table(u'caroftheday_car', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('imageLink', self.gf('django.db.models.fields.FilePathField')(max_length=100)),
            ('link', self.gf('django.db.models.fields.FilePathField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('make', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'caroftheday', ['Car'])


    def backwards(self, orm):
        # Deleting model 'Car'
        db.delete_table(u'caroftheday_car')


    models = {
        u'caroftheday.car': {
            'Meta': {'object_name': 'Car'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'imageLink': ('django.db.models.fields.FilePathField', [], {'max_length': '100'}),
            'link': ('django.db.models.fields.FilePathField', [], {'max_length': '100'}),
            'make': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['caroftheday']