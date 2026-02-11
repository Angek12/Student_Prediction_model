from rest_framework import serializers
from .models import StudentPerformance


class StudentPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPerformance
        # Only the input features should be writable from the client.
        # performance_index is predicted by the model, so keep it read-only.
        fields = [
            'hours_studied',
            'previous_scores',
            'extracurricular',
            'sleep_hours',
            'sample_papers',
            'performance_index',
        ]
        read_only_fields = ('performance_index',)

    def validate(self, data):
        hours_studied = data.get('hours_studied', 0)
        sleep_hours = data.get('sleep_hours', 0)

        total_hours = hours_studied + sleep_hours
        if total_hours > 24:
            raise serializers.ValidationError(
                f'Total hours studied and sleep ({total_hours}) cannot exceed 24 hours in a day.'
            )

        return data
