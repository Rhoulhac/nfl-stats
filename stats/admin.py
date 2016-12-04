from django.contrib import admin

from stats.models import Team, Location, Quaterback

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'mascot', 'team_location')
    search_fields = ('name', )

    def team_location(self, obj):
        return '{}, {}'.format(obj.location.city, obj.location.state)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('state', 'city')
    list_filter = ('state', )



class QuaterbackAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'qb_team')

    def qb_team(self, obj):
        return '{}'.format(obj.team.name)

admin.site.register(Team, TeamAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Quaterback, QuaterbackAdmin)
