from django.db import models

# Create your models here.
class candidate(models.Model):
    Fullname=models.CharField(max_length=100)
    Age=models.IntegerField()
    Experience=models.CharField(max_length=100)
    Current_Company=models.CharField(max_length=100)
    Email=models.EmailField(max_length=254)
    Skills=models.TextField(max_length=200)
    CV=models.FileField(upload_to=None, max_length=100)

    def __str__(self):
        return self.Fullname
    
    class meta:
        db_table="Candidatess"

class Panel_member(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=254)
    Designation=models.CharField(max_length=100)

    def __str__(self):
        return self.Name
    
    class meta:
        db_table="panel_members"

        
class master_interview(models.Model):
    Interview_rd= models.IntegerField()
    candidate_id=models.ForeignKey(candidate, on_delete=models.CASCADE)
    Job_position=models.CharField(max_length=100)
    Status=models.CharField(max_length=50)
    Panelmember=models.ForeignKey(Panel_member, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=100)
    ispromoted=models.BooleanField(default=False)

    class meta:
        db_table="master_interview"

    

   

    



    