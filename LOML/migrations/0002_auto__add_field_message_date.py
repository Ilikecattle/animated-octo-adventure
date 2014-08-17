# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Message.date'
        db.add_column(u'LOML_message', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 8, 17, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Message.date'
        db.delete_column(u'LOML_message', 'date')


    models = {
        u'LOML.message': {
            'Meta': {'object_name': 'Message'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['LOML']