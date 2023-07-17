from django.db import models

# مدل اطلاعات قطعه
class Component(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField()
    area = models.FloatField()
    blooming_time_choices = [
        ('early', 'زودگل'),
        ('medium', 'متوسط گل'),
        ('late', 'دیر گل')
    ]
    blooming_time = models.CharField(max_length=10, choices=blooming_time_choices)
    male_tree_density = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)
    last_modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


# مدل اطلاعات اب مصرفی
class WaterConsumption(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    consumption = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.component} - {self.date}"


# مدل اطلاعات یخ اب زمستانه
class WinterWater(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    consumption = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.component} - {self.date}"


# مدل اطلاعات انالیز خاک
class SoilAnalysis(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.component} - {self.date}"


# مدل اطلاعات آفت غالب
class Pest(models.Model):
    PEST_TYPES = [
        ('sen', 'سن'),
        ('psil', 'پسیل'),
        ('sank', 'سنک'),
        ('kermania', 'کرمانیا')
    ]
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    date = models.DateField()
    pest_type = models.CharField(max_length=10, choices=PEST_TYPES)

    def __str__(self):
        return f"{self.component} - {self.date}"


# مدل اطلاعات کود مصرفی
class Fertilizer(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    consumption = models.FloatField()
    date = models.DateField()
    fertilizer_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.component} - {self.date}"


# مدل اطلاعات برداشت
class Harvest(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    date = models.DateField()
    harvest_amount = models.FloatField()
    cluster_defect_percentage = models.FloatField()
    cluster_yield = models.FloatField()
    annual_yield = models.FloatField()

    def __str__(self):
        return f"{self.component} - {self.date}"


# مدل اطلاعات باغ
class Orchard(models.Model):
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
