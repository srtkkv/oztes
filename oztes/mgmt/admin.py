from django.contrib import admin
from .models import Policy,Emp,OU,Policy_applied_to_OU, Policy_appied_to_Emp

admin.site.register(Policy)
admin.site.register(Emp)
admin.site.register(OU)
admin.site.register(Policy_applied_to_OU)
admin.site.register(Policy_appied_to_Emp)