from rest_framework import serializers
from Component_table.models import Component,WaterConsumption,WinterWater,SoilAnalysis,Pest,Fertilizer,Harvest,Orchard

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'

class WaterConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterConsumption
        fields = '__all__'

class WinterWaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = WinterWater
        fields = '__all__'

class SoilAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoilAnalysis
        fields = '__all__'

class PestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pest
        fields = '__all__'

class FertilizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fertilizer
        fields = '__all__'

class HarvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Harvest
        fields = '__all__'

class OrchardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orchard
        fields = '__all__'