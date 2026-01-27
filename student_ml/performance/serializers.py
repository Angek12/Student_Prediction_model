from rest_framework import serializers
from .models import StudentPerformance


class StudentPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPerformance
        fields = '__all__'

    def validate(self, data):
        hours_studied = data.get('hours_studied', 0)
        sleep_hours = data.get('sleep_hours', 0)
        
        total_hours = hours_studied + sleep_hours
        if total_hours > 24:
            raise serializers.ValidationError(
                f'Total hours studied and sleep ({total_hours}) cannot exceed 24 hours in a day.'
            )
        
        return data
