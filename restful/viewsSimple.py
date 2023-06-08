import datetime
import json
import locale
from django.http import Http404, JsonResponse
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import News, Profile, BookingModel
from .serializers import NewsSerializer, ProfileSerializer, UserProfilSerializer, BookingSerializer


class NewsAPIList(generics.ListAPIView):
    model = News
    queryset = News.objects.filter(is_published=True)
    serializer_class = NewsSerializer


class NewsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated, )


# Register API
class RegisterAPI(generics.GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
        "msq": "user created"
        })


#Get user by username
class RetriveProfileView(viewsets.ViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Profile.objects.all()

    @action(detail=False, methods=['get'])
    def retrieve(self, request, username):
        item = get_object_or_404(self.queryset, username=username)
        serializer = ProfileSerializer(item)
        return Response(serializer.data)


def booking_order_green(request):

    if request.method == "GET":
        respData = []
        today = datetime.datetime.now()
        date = today + datetime.timedelta(days=7)
        qs = BookingModel.objects.filter(booking_date__range=[today, date], cort=1).order_by("booking_date", "period")
        for record in qs:
            dictRec = {
                "period": record.period,
                "cort": record.cort,
                "booking_date": record.booking_date,
                "user": record.user.__str__()
            }
            respData.append(dictRec)
        print(respData)
        return JsonResponse(respData, safe=False)

    if request.method == "POST":
        pass

