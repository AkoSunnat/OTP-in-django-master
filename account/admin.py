from django.contrib import admin
from account.models import Account
from verification.models import phoneModel

class AccountAdmin(admin.ModelAdmin):
    list_display=("user","phone_number","visit_counter")

admin.site.register(Account,AccountAdmin)