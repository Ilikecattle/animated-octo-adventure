# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Message.text'
        db.alter_column(u'LOML_message', 'text', self.gf('django.db.models.fields.CharField')(max_length=1000))

    def backwards(self, orm):

        # Changing field 'Message.text'
        db.alter_column(u'LOML_message', 'text', self.gf('django.db.models.fields.CharField')(max_length=100))

    models = {
        u'LOML.message': {
            'Meta': {'object_name': 'Message'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        }
    }

    complete_apps = ['LOML']