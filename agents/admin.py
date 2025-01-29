from django.contrib import admin
from .models import Agent, Ability

class AbilityInline(admin.TabularInline):
    model = Ability
    extra = 4  # Štandardne zobrazí štyri riadky na pridanie schopností

class AgentAdmin(admin.ModelAdmin):
    inlines = [AbilityInline]

admin.site.register(Agent, AgentAdmin)
admin.site.register(Ability)