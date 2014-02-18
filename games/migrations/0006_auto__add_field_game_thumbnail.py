# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Game.thumbnail'
        db.add_column(u'games_game', 'thumbnail',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Game.thumbnail'
        db.delete_column(u'games_game', 'thumbnail')


    models = {
        u'games.category': {
            'Meta': {'object_name': 'Category'},
            'games': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['games.Game']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'games.game': {
            'Meta': {'object_name': 'Game'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['games.Category']", 'symmetrical': 'False', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'platform': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'thumbnail': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['games']