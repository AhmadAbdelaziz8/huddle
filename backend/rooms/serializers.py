from rest_framework import serializers

from .models import Room


# 1. FIXED: Must use ModelSerializer to use the Meta class.
# Regular 'Serializer' ignores the Meta class entirely.
class RoomSerializer(serializers.ModelSerializer):
    # createed on the fly 
    join_url = serializers.SerializerMethodField() 

    class Meta:
        model = Room
        fields = ["id", "created_at", "is_active", "join_url"] 

    def get_join_url(self, obj):
        request = self.context.get("request")
        # 4. FIXED: The correct Django method is build_absolute_uri(), not build_absolute_url().
        # Also fixed the localhost port formatting.
        base_url = request.build_absolute_uri('/') if request else 'http://localhost:8000/'
        return f"{base_url}{obj.id}"