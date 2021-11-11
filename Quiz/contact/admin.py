from django.contrib import admin
from .models import FAQ, ContactUs


# Register your models here.
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)
    prepopulated_fields = {'slug': ('question',)}


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('type', 'email', 'replied_at')


admin.site.register(FAQ, FAQAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
