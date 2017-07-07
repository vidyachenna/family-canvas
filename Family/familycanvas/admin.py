from django.contrib import admin
#from .models import profile
from .models import story
from .models import events
from .models import gallery
from .models import Family_tree
from .models import groups

admin.site.register(Family_tree)
admin.site.register(gallery)
admin.site.register(events)
admin.site.register(story)
#admin.site.register(profile)
admin.site.register(groups)
# Register your models here.
