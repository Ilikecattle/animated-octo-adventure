# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Question'
        db.create_table(u'carquizgame_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('car', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['caroftheday.Car'])),
            ('numCorrect', self.gf('django.db.models.fields.IntegerField')()),
            ('numIncorrect', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'carquizgame', ['Question'])


    def backwards(self, orm):
        # Deleting model 'Question'
        db.delete_table(u'carquizgame_question')


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
        },
        u'carquizgame.question': {
            'Meta': {'object_name': 'Question'},
            'car': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['caroftheday.Car']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numCorrect': ('django.db.models.fields.IntegerField', [], {}),
            'numIncorrect': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['carquizgame']