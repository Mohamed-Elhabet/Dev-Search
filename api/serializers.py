from rest_framework import serializers
from projects.models import Project, Tag, Review
from users.models import Profile 

class ReviewSerializer(serializers.ModelSerializer):
  class Meta:
    model = Review
    fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
  owner = ProfileSerializer(many=False) # (nested relationship)
  tags = TagSerializer(many=True)
  # to get reviews into a project
  reviews = serializers.SerializerMethodField()
  class Meta:
    model = Project 
    fields = '__all__'

  # always have to start our methods with get 
  def get_reviews(self, obj): 
    '''self not refer to model, but to serializer class (projectSerializers)
    obj -> object that we're serializing, which will be this project 
    '''
    reviews = obj.review_set.all() # project.review_set.all()
    serializer = ReviewSerializer(reviews, many=True)
    return serializer.data 