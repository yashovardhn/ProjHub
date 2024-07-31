from django.db import models
import uuid
from ulist_user.models import Profile
# Create your models here.
class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete= models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000 , null=True, blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    votes_ratio = models.IntegerField(default=0, null=True, blank=True)
    tag = models.ManyToManyField('Tag', blank=True)  #many to mnay relationship
    creted = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['creted']

    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset



    @property
    def get_vote_count(self):
        reviews = self.review_set.all()
        upvotes = reviews.filter(value ='up').count()
        # downvotes = reviews.filter(value='down')
        total_votes = reviews.count()

        ratio = (upvotes / total_votes) * 100
        self.vote_total = total_votes
        self.votes_ratio = ratio
        self.save()
    
class Review(models.Model):
    vote_type = (
        ('up', 'Upvote'),
        ('down', 'Downvote'),
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE) 
    body = models.TextField(null= True, blank=True)
    value = models.TextField(max_length= 200, choices= vote_type)
    vote_total = models.IntegerField(default=0, null= True, blank=True)
    vote_ratio = models.IntegerField(default=0, null= True, blank=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True, editable=False) #one to manay relationship

    class Meta:
        unique_together = [['owner', 'project']]
    def __str__(self):
        return self.value
    

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True) 
    id =  models.UUIDField(default=uuid.uuid4,unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
