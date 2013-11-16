# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Activity'
        db.delete_table(u'meetme_activity')

        # Adding model 'Reservation'
        db.create_table(u'meetme_reservation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('local', self.gf('django.db.models.fields.related.ForeignKey')(related_name='local', to=orm['meetme.Account'])),
            ('visitor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='visitor', to=orm['meetme.Account'])),
            ('day', self.gf('django.db.models.fields.IntegerField')()),
            ('time_range', self.gf('django.db.models.fields.IntegerField')()),
            ('local_response', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'meetme', ['Reservation'])

        # Adding field 'Account.category'
        db.add_column(u'meetme_account', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['meetme.Category'], null=True),
                      keep_default=False)

        # Adding field 'Account.available'
        db.add_column(u'meetme_account', 'available',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Activity'
        db.create_table(u'meetme_activity', (
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['meetme.Category'])),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['meetme.Account'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('tagline', self.gf('django.db.models.fields.CharField')(max_length=140)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'meetme', ['Activity'])

        # Deleting model 'Reservation'
        db.delete_table(u'meetme_reservation')

        # Deleting field 'Account.category'
        db.delete_column(u'meetme_account', 'category_id')

        # Deleting field 'Account.available'
        db.delete_column(u'meetme_account', 'available')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'meetme.account': {
            'Meta': {'object_name': 'Account'},
            'available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['meetme.Category']", 'null': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('phonenumber_field.modelfields.PhoneNumberField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tagline': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'meetme.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'meetme.reservation': {
            'Meta': {'object_name': 'Reservation'},
            'day': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'local'", 'to': u"orm['meetme.Account']"}),
            'local_response': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'time_range': ('django.db.models.fields.IntegerField', [], {}),
            'visitor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'visitor'", 'to': u"orm['meetme.Account']"})
        },
        u'meetme.review': {
            'Meta': {'object_name': 'Review'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['meetme.Account']"}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'review_author'", 'to': u"orm['meetme.Account']"}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['meetme']