from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def basic_validator(self, postData, type, show_id=None):
        errors = {}
        if show_id:
            show = Show.objects.get(id=show_id)
        if len(postData['title']) < 2:
            errors['name'] = 'Title should be at least 2 characters'
        if len(postData['network']) < 3:
            errors['network'] = 'Network should be at least 3 characters'
        if len(postData['description']) > 0:
            if len(postData['description']) < 10:
                errors['description'] = 'Description should be at least 10 characters'
        titles=Show.objects.filter(title=postData['title'])
        # if type == 'edit':
        if len(titles) > 0:
            if type =='edit':
                if not show.title == postData['title']:
                    errors['title']='This show already exists'
            else: 
                errors['title']='This show already exists'
        today = datetime.today()
        release_date=datetime.strptime(postData['release_date'], '%Y-%m-%d')
        if release_date>today:
            errors['release_date']='Release date should be in the past'
        return errors

    # def title_valitator(self, postData):
    #     errors={}
    #     if len(postData['title']) < 2:
    #         errors['name'] = 'Title should be at least 2 characters'
    #     if len(postData['network']) < 3:
    #         errors['network'] = 'Network should be at least 3 characters'
    #     if len(postData['description']) > 0:
    #         if len(postData['description']) < 10:
    #             errors['description'] = 'Description should be at least 10 characters'
    #     today = datetime.today()
    #     release_date=datetime.strptime(postData['release_date'], '%Y-%m-%d')
    #     if release_date>today:
    #         errors['release_date']='Release date should be in the past'
    #     return errors


class Network(models.Model):
    name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Show(models.Model):
    title=models.CharField(max_length=255)
    network=models.ForeignKey(Network, related_name='shows', on_delete=models.CASCADE)
    description=models.TextField()
    release_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=ShowManager()
