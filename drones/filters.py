import django_filters as filters

from drones.models import Competition


class CompetitionFilter(filters.FilterSet):
    from_achievement_date = filters.DateTimeFilter(name='distance_achievement_date', lookup_expr='gte')
    to_achievement_date = filters.DateTimeFilter(name='distance_achievement_date', lookup_expr='lte')
    min_distance_in_feet = filters.NumberFilter(name='distance_in_feet', lookup_expr='gte')
    max_distance_in_feet = filters.NumberFilter(name='distance_in_feet', lookup_expr='lte')
    drone_name = filters.AllValuesFilter(name='drone__name')
    pilot_name = filters.AllValuesFilter(name='pilot__name')

    class Meta:
        model = Competition
        fields = ('distance_in_feet', 'from_achievement_date', 'to_achievement_date', 'min_distance_in_feet',
                  'max_distance_in_feet', 'drone_name', 'pilot_name',)
