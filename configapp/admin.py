from django.contrib import admin
from configapp.models import *

admin.site.register([Status, Transaction, Type,Category,Subcategory])
