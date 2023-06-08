from .models import *
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = "__all__"


# Using ChoiceField
class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        # To support inserts with the value
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=Profile.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    gender = ChoiceField(choices=Profile.GENDER_CHOICES)

    class Meta:
        model = Profile
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "gender",
            "city",
            "phone",
            "photo",
            "password",
            "birth_date"
        ]
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def create(self, validated_data):
        user = Profile.objects.create(
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            gender=validated_data["gender"],
            city=validated_data["city"],
            phone=validated_data["phone"],
            photo=validated_data["photo"],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user


class UserProfilSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [
            "id",
            "first_name",
            "last_name"
        ]


class BookingModelGreenSerializer(serializers.ModelSerializer):
    # user = UserProfilSerializer

    class Meta:
        model = BookingModelGreen
        fields = [
            "period",
            "booking_date",
            "cort",
            "user"
        ]