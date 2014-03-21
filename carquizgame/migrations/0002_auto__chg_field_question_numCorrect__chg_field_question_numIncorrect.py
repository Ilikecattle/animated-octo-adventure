# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Question.numCorrect'
        db.alter_column(u'carquizgame_question', 'numCorrect', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Question.numIncorrect'
        db.alter_column(u'carquizgame_question', 'numIncorrect', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'Question.numCorrect'
        db.alter_column(u'carquizgame_question', 'numCorrect', self.gf('django.db.models.fields.IntegerField')(default=0))

        # Changing field 'Question.numIncorrect'
        db.alter_column(u'carquizgame_question', 'numIncorrect', self.gf('django.db.models.fields.IntegerField')(default=0))

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
            'numCorrect': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'numIncorrect': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['carquizgame']