from django.contrib import admin
from .models import *
class CallbackFormAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'phone',
        'product',
        'is_done',
        'created_at',
    )

    list_filter = (
        'is_done',
    )
    model = CallbackForm


admin.site.register(Banner)
admin.site.register(Faq)
admin.site.register(CallbackForm,CallbackFormAdmin)