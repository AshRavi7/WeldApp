from django.contrib import admin
from .models import project,location_discipline,weld_action,heat_calc,drawing,weld,gallery,activity_description,activity_inspection_action,Profile

admin.site.register(project)
admin.site.register(location_discipline)
admin.site.register(weld_action)
admin.site.register(heat_calc)
admin.site.register(drawing)
admin.site.register(weld)
admin.site.register(gallery)
admin.site.register(activity_description)
admin.site.register(activity_inspection_action)
admin.site.register(Profile)
