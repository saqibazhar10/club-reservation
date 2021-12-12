from django.contrib import admin

# Register your models here.
from .models import Manager, Payment, Registered_User,Reservation,feedback,events,Room,Message, feedback
# ,Room,Message

admin.site.register(Registered_User)
admin.site.register(Reservation)
admin.site.register(Manager)
admin.site.register(Payment)
admin.site.register(feedback)
admin.site.register(events)
admin.site.register(Room)
admin.site.register(Message)