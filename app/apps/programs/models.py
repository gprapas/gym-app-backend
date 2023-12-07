from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from enum import Enum


class muscle_groups_types(Enum):
    chest = "Chest"
    back = "Back"
    legs = "Legs"
    shoulders = "Shoulders"
    biceps = "Biceps"
    triceps = "Triceps"

class chest(Enum):
    BenchPress = "Bench Press"
    InclineBenchPress = "Incline Bench Press"
    DeclineBenchPress = "Decline Bench Press"
    DumbbellPress = "Dumbbell Press"
    PushUps = "Push-ups"
    Dips = "Dips"
    Flyes = "Flyes"
    CableCrossover = "Cable Crossover"

class BackExercises(Enum):
    PullUps = "Pull-ups"
    Deadlifts = "Deadlifts"
    BentOverRows = "Bent Over Rows"
    LatPulldowns = "Lat Pulldowns"
    FacePulls = "Face Pulls"

class LegExercises(Enum):
    Squats = "Squats"
    Lunges = "Lunges"
    Deadlifts = "Deadlifts"
    LegPress = "Leg Press"
    LegCurls = "Leg Curls"

class ShoulderExercises(Enum):
    OverheadPress = "Overhead Press"
    LateralRaises = "Lateral Raises"
    FrontRaises = "Front Raises"
    Shrugs = "Shrugs"
    FacePulls = "Face Pulls"

class BicepExercises(Enum):
    BarbellCurls = "Barbell Curls"
    DumbbellCurls = "Dumbbell Curls"
    HammerCurls = "Hammer Curls"
    ConcentrationCurls = "Concentration Curls"
    PreacherCurls = "Preacher Curls"

class TricepExercises(Enum):
    TricepDips = "Tricep Dips"
    TricepExtensions = "Tricep Extensions"
    CloseGripBenchPress = "Close Grip Bench Press"
    SkullCrushers = "Skull Crushers"
    OverheadTricepExtensions = "Overhead Tricep Extensions"



class GymFile(models.Model):
    title = models.CharField(max_length=30)
    document = models.FileField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Gym Programs'


class AvailiableExercises(models.Model):
    name = models.CharField(max_length=60)
    type = models.CharField(max_length=40,choices=
                                    [(choice.name, choice.value) for choice in muscle_groups_types])
    
    def __str__(self):
        return self.name + " (" + self.type.capitalize() +")"
    
    class Meta:
        verbose_name_plural = 'Availiable Exercises'


class Program(models.Model):
    type = models.CharField(max_length=50)
    comments = models.TextField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type
    

class Days(models.Model):
    exercise = models.ManyToManyField(AvailiableExercises, through='DaysExercises')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    muscle_group = models.CharField(max_length=50, choices=
                                    [(choice.name, choice.value) for choice in muscle_groups_types])

    def __str__(self):
        return self.muscle_group
    
    
    class Meta:
        verbose_name_plural = 'Days'





class DaysExercises(models.Model):
    day = models.ForeignKey(Days, on_delete=models.CASCADE)
    exercise = models.ForeignKey(AvailiableExercises, on_delete=models.CASCADE)
    sets = models.IntegerField()
    reps = models.IntegerField()
    rpe = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    tempo = models.CharField(max_length=50)

    class Meta:
        unique_together = ['day', 'exercise']
