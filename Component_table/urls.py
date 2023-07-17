from django.urls import path
from Component_table import views

urlpatterns = [
    path('components/', views.ComponentList.as_view(), name='component-list'),
    path('components/<int:pk>/', views.ComponentDetail.as_view(), name='component-detail'),
    path('WaterConsumptions/', views.WaterConsumptionList.as_view(), name='WaterConsumption-list'),
    path('WaterConsumptions/<int:pk>/', views.WaterConsumptionDetail.as_view(), name='WaterConsumption-detail'),
    path('WinterWaters/', views.WinterWaterList.as_view(), name='WinterWater-list'),
    path('WinterWaters/<int:pk>/', views.WinterWaterDetail.as_view(), name='WinterWater-detail'),
    path('SoilAnalysis/', views.SoilAnalysisList.as_view(), name='SoilAnalysis-list'),
    path('SoilAnalysis/<int:pk>/', views.SoilAnalysisDetail.as_view(), name='SoilAnalysis-detail'),
    path('Pests/', views.PestList.as_view(), name='Pest-list'),
    path('Pests/<int:pk>/', views.PestDetail.as_view(), name='Pest-detail'),
    path('Fertilizers/', views.FertilizerList.as_view(), name='Fertilizer-list'),
    path('Pests/<int:pk>/', views.FertilizerDetail.as_view(), name='Fertilizer-detail'),
    path('Harvests/', views.HarvestList.as_view(), name='Harvest-list'),
    path('Harvests/<int:pk>/', views.HarvestDetail.as_view(), name='Harvest-detail'),
    path('Orchards/', views.OrchardList.as_view(), name='Orchard-list'),
    path('Orchards/<int:pk>/', views.OrchardDetail.as_view(), name='Orchard-detail'),

]
