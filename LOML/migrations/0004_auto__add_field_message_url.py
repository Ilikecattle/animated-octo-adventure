# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Message.url'
        db.add_column(u'LOML_message', 'url',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=1000),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Message.url'
        db.delete_column(u'LOML_message', 'url')


    models = {
        u'LOML.message': {
            'Meta': {'object_name': 'Message'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '1000'})
        }
    }

    complete_apps = ['LOML']