# Copyright (c) 2019 Ezybaas by Bhavik Shah.
# Susthitsoft Technologies Private Limited.
# All rights reserved.
# Please see the LICENSE.txt included as part of this package.

import os
from . import appslist
from django.conf import settings

BASE_DIR = settings.BASE_DIR
EZYBAAS_DATABASES = {
	'production': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'ezybaas.prod.db'),
	},
	'staging': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'ezybaas.staging.db'),
	},
	'test': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'ezybaas.test.db'),
	},
	'ezybaas': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'ezybaas.db'),
	}
}

DATABASE_APPS_MAPPING = {'contenttypes': 'default',
                     'auth': 'default',
                     'admin': 'default',
                     'sessions': 'default',
                     'messages': 'default',
                     'staticfiles': 'default',
                     'ezybaas': 'ezybaas',
                     }

class EzyBaasDbRouter:

    """
    A router to control all database operations on models in the
    ezybaas application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read ezybaas models go to ezybaas_db.
        """
        if model._meta.app_label in appslist.APPS_LIST:
            # print('APPS DB')('read'+appslist.APPS_DB_LABEL)
            return appslist.APPS_DB_LABEL
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write ezybaas models go to ezybaas_db.
        """
        if model._meta.app_label in appslist.APPS_LIST:
            #print('APPS DB')('write'+appslist.APPS_DB_LABEL)
            return appslist.APPS_DB_LABEL
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the ezybaas app is involved.
        """
        # Allow relations between two models that are both Django core app models
        if obj1._meta.app_label in ['auth','admin','sessions','contenttypes'] and obj2._meta.app_label in ['auth','admin','sessions','contenttypes']:
            return True
        elif obj1._meta.app_label in appslist.APPS_LIST and \
            obj2._meta.app_label in appslist.APPS_LIST:
            #print('APPS DB')('relation'+appslist.APPS_DB_LABEL)
            return True
        # If neither object is in a Django core app model (defer to other routers or default database)
        elif obj1._meta.app_label not in ['auth','admin','sessions','contenttypes'] or obj2._meta.app_label not in ['auth','admin','sessions','contenttypes']:
            return None
        return None

        # OLD CODE
        if obj1._meta.app_label in appslist.APPS_LIST and \
           obj2._meta.app_label in appslist.APPS_LIST:
            ##print('APPS DB')('APPS DB')('relation'+appslist.APPS_DB_LABEL)
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the ezybaas app only appears in the 'ezybaas_db'
        database.
        """

        if db in settings.DATABASE_APPS_MAPPING.values():
            ##print('APPS DB')('APPS DB')(db+':' + app_label +' => migrate => '+str(settings.DATABASE_APPS_MAPPING.get(app_label) == db))
            return settings.DATABASE_APPS_MAPPING.get(app_label) == db
        elif app_label in settings.DATABASE_APPS_MAPPING:
            ##print('APPS DB')('APPS DB')('False')
            return False

        #OLD CODE 
        if db == appslist.APPS_DB_LABEL and app_label in appslist.APPS_LIST:
            ##print('APPS DB')('APPS DB')('migrate'+appslist.APPS_DB_LABEL)
            return True
        
        return None

