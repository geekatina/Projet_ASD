import datetime
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    PRIORITIES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    
    description = models.CharField(max_length=200)
    deadline = models.DateField()
    priority = models.IntegerField(choices=PRIORITIES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    def calculate_priority(self):
        days_until_deadline = (self.deadline - datetime.date.today()).days
        if days_until_deadline <= 0:
            return 5  # Priorité très élevée pour les tâches dépassées
        elif days_until_deadline <= 2:
            return 4  # Priorité élevée pour les tâches avec une date limite proche
        elif days_until_deadline <= 7:
            return 3  # Priorité normale pour les tâches à venir dans la semaine
        else:
        # Calculer la priorité en fonction du nombre de jours restants
            return min(5, max(1, 5 - (days_until_deadline // 7)))



# category
# description
# deadline
# priorite