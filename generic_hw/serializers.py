from rest_framework.serializers import ModelSerializer
from .models import Hw

class HwSerializer(ModelSerializer):
    class Meta :
        model = Hw
        fields = '__all__'