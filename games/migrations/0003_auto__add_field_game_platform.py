# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Game.platform'
        db.add_column(u'games_game', 'platform',
                      self.gf('django.db.models.fields.CharField')(default='Flash', max_length=5),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Game.platform'
        db.delete_column(u'games_game', 'platform')


    models = {
        u'games.game': {
            'Meta': {'object_name': 'Game'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'platform': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'width': ('django.db.models.fields.IntegerField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['games']