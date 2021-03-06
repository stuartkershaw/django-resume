from django.contrib.auth.models import User, Group
from rest_framework import serializers

from resume.models import Interest, Company, Position, School, Program, Course,\
                          Institution, Certification, Project, Profile, Website


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'name', 'email', 'location', 'about')


class WebsiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Website
        fields = ('name', 'url')


class InterestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interest
        fields = ('name', 'order_id')


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'location', 'url', 'order_id')


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ('title', 'description', 'company', 'is_current',
                  'start_date', 'end_date')


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ('name', 'location', 'url', 'order_id')


class ProgramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Program
        fields = ('name', 'url', 'degree', 'description', 'school',
                  'is_current', 'start_date', 'end_date')


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'url', 'description', 'program')


class InstitutionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Institution
        fields = ('name', 'url', 'order_id')


class CertificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Certification
        fields = ('name', 'url', 'description', 'institution', 'will_expire',
                  'valid_from', 'valid_to')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'url', 'description')
