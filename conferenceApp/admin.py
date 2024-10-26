from typing import Any
from django.contrib import admin
from .models import Conference
from django.utils import timezone
from userApp.models import Reservation

# Register your models here.

class ReservationInline(admin.StackedInline):
    model = Reservation
    extra = 2
    can_delete = False
    readonly_fields = ('reservation_date',)

class ConferenceDateFilter(admin.SimpleListFilter):
    title = "Conference Date"
    parameter_name = 'conference_date'
    def lookups(self, request, queryset):
        return (
            ('past', 'Past Conferences'),
            ('upcoming', 'Upcoming Conferences'),
            ('today', 'Today Conferences'),
        )
    def queryset(self, request, queryset):
        today = timezone.now().date()
        if self.value() == 'past':
            return queryset.filter(end_date__lt = today)
        if self.value() == 'upcoming':
            return queryset.filter(start_date__gt = today)
        if self.value() == 'today':
            return queryset.filter(start_date = today)
        return queryset

class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'location', 'price')
    ordering = ('title', 'start_date')
    list_per_page = 1
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Description',
        {
            'fields': ('title', 'description')
        }
        ),
        ('Horaires',
        {
            'fields': ('start_date', 'end_date')
        }
        ),
        ('Informations de la conférence', {
            'fields': ('location', 'price', 'capacity'),
        }),
        ('Documents', {
            'fields': ('program',),
        }),
        ('Catégorie', {
            'fields': ('category',),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            
        }),
        
    )
    
    list_filter = ('title', ConferenceDateFilter)
    search_fields = ('title', 'location',)
    autocomplete_fields = ('category',)
    inlines = [ReservationInline]
    


admin.site.register(Conference, ConferenceAdmin)