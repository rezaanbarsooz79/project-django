from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics
from Component_table.models import Component
from Component_table.serializers import ComponentSerializer,WaterConsumptionSerializer,WinterWaterSerializer,SoilAnalysisSerializer,PestSerializer,FertilizerSerializer,HarvestSerializer,OrchardSerializer
from .models import Component,WaterConsumption,WinterWater,SoilAnalysis,Pest,Fertilizer,Harvest,Orchard


def post_list(request):
    Components=Component.objects.all()
    WaterConsumptions_data=WaterConsumption.objects.all()
    WinterWaters_data=WinterWater.objects.all()
    SoilAnalysises_data=SoilAnalysis.objects.all()
    Pestes_data=Pest.objects.all()
    Fertilizers_data=Fertilizer.objects.all()
    Harvestes_data=Harvest.objects.all()
    Orchards_data=Orchard.objects.all()
    context={'Components':Components,
'WaterConsumptions_data':WaterConsumptions_data,
'WinterWaters_data':WinterWaters_data,
'SoilAnalysises_data':SoilAnalysises_data,
'Pestes_data':Pestes_data,
'Fertilizers_data':Fertilizers_data,
'Harvestes_data':Harvestes_data,
'Orchards_data':Orchards_data
}

    return render(request,'Components/index.html',context)

class ComponentList(generics.ListCreateAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

class ComponentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

class WaterConsumptionList(generics.ListCreateAPIView):
    queryset = WaterConsumption.objects.all()
    serializer_class = WaterConsumptionSerializer

class WaterConsumptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WaterConsumption.objects.all()
    serializer_class = WaterConsumptionSerializer

class WinterWaterList(generics.ListCreateAPIView):
    queryset = WinterWater.objects.all()
    serializer_class = WinterWaterSerializer

class WinterWaterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WinterWater.objects.all()
    serializer_class = WinterWaterSerializer

class SoilAnalysisList(generics.ListCreateAPIView):
    queryset = SoilAnalysis.objects.all()
    serializer_class = SoilAnalysisSerializer

class SoilAnalysisDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SoilAnalysis.objects.all()
    serializer_class = SoilAnalysisSerializer

class PestList(generics.ListCreateAPIView):
    queryset = Pest.objects.all()
    serializer_class = PestSerializer

class PestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pest.objects.all()
    serializer_class = PestSerializer

class FertilizerList(generics.ListCreateAPIView):
    queryset = Fertilizer.objects.all()
    serializer_class = FertilizerSerializer

class FertilizerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fertilizer.objects.all()
    serializer_class = FertilizerSerializer

class HarvestList(generics.ListCreateAPIView):
    queryset = Harvest.objects.all()
    serializer_class = HarvestSerializer

class HarvestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Harvest.objects.all()
    serializer_class = HarvestSerializer

class OrchardList(generics.ListCreateAPIView):
    queryset = Orchard.objects.all()
    serializer_class = OrchardSerializer

class OrchardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orchard.objects.all()
    serializer_class = OrchardSerializer