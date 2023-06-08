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
        period = {
            "06:00 - 07:00": 0,
            "07:00 - 08:00": 1,
            "08:00 - 09:00": 2,
            "09:00 - 10:00": 3,
            "10:00 - 11:00": 4,
            "11:00 - 12:00": 5,
            "12:00 - 13:00": 6,
            "13:00 - 14:00": 7,
            "14:00 - 15:00": 8,
            "15:00 - 16:00": 9,
            "16:00 - 17:00": 10,
            "17:00 - 18:00": 11,
            "18:00 - 19:00": 12,
            "19:00 - 20:00": 13,
            "20:00 - 21:00": 14,
            "21:00 - 22:00": 15
        }
        gridData = [
            {"period": "06:00 - 07:00", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: ""},
            {"period": "07:00 - 08:00", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: ""},
            {"period": "08:00 - 09:00", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: ""},
            {"period": "09:00 - 10:00", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: ""},
            {"period": "10:00 - 11:00", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: ""},
            {"period": "11:00 - 12:00", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: ""},
            {"period": "12:00 - 13:00", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: ""},
            {"period": "13:00 - 14:00", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: ""},
            {"period": "14:00 - 15:00", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: ""},
            {"period": "15:00 - 16:00", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: ""},
            {"period": "16:00 - 17:00", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: ""},
            {"period": "17:00 - 18:00", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: ""},
            {"period": "18:00 - 19:00", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: ""},
            {"period": "19:00 - 20:00", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: ""},
            {"period": "20:00 - 21:00", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: ""},
            {"period": "21:00 - 22:00", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: ""}
        ]
        locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')
        today = datetime.datetime.now()
#        days = []
        for i in range(8):
            date = today + datetime.timedelta(days=i)
#            days.append(date.strftime('%A') + ", " + date.strftime('%d-%m-%Y'))
            booking = BookingModel.objects.filter(booking_date=date, cort=1)
            for record in booking:
                gridData[period[record.period]][i+1] = record.user.__str__()
        return JsonResponse(gridData, safe=False)

    if request.method == "POST":
        periodList = [
            "06:00 - 07:00",
            "07:00 - 08:00",
            "08:00 - 09:00",
            "09:00 - 10:00",
            "10:00 - 11:00",
            "11:00 - 12:00",
            "12:00 - 13:00",
            "13:00 - 14:00",
            "14:00 - 15:00",
            "15:00 - 16:00",
            "16:00 - 17:00",
            "17:00 - 18:00",
            "18:00 - 19:00",
            "19:00 - 20:00",
            "20:00 - 21:00",
            "21:00 - 22:00"
        ]
        dataToSave = json.loads(request.body)
        datePeriod = dataToSave["bookingid"].split("_")
        day = int(datePeriod[0]) - 1
        booking_date = datetime.datetime.now() + datetime.timedelta(days=day)
        period = periodList[int(datePeriod[1])-1]
        cort = "1"
        user = Profile.objects.get(id=dataToSave["userid"])
        BookingModel.objects.create(
            period=period,
            cort=cort,
            booking_date=booking_date,
            user=user
        )
        return JsonResponse({"msg": "That is good"}, safe=False)

