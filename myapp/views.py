from rest_framework import generics
from .models import GeneralPost, SardorPost, ZoirPost, JasurPost
from .serializers import GeneralPostSerializer, SardorPostSerializer, ZoirPostSerializer, JasurPostSerializer

# Sardor API (faqat POST va GET o'ziga)
class SardorPostView(generics.ListCreateAPIView):
    queryset = SardorPost.objects.all()
    serializer_class = SardorPostSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        GeneralPost.objects.create(**serializer.validated_data)

# Zoir API (faqat POST va GET o'ziga)
class ZoirPostView(generics.ListCreateAPIView):
    queryset = ZoirPost.objects.all()
    serializer_class = ZoirPostSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        GeneralPost.objects.create(**serializer.validated_data)

# Jasur API (faqat POST va GET o'ziga)
class JasurPostView(generics.ListCreateAPIView):
    queryset = JasurPost.objects.all()
    serializer_class = JasurPostSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        GeneralPost.objects.create(**serializer.validated_data)

# Umumiy API (faqat GET, POST YO‘Q)
class GeneralPostListView(generics.ListAPIView):
    queryset = GeneralPost.objects.all()
    serializer_class = GeneralPostSerializer

# UPDATE va DELETE API (General dan o‘zgartirilsa, boshqalar ham o‘zgaradi yoki o‘chadi)
class GeneralPostUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GeneralPost.objects.all()
    serializer_class = GeneralPostSerializer

    def perform_update(self, serializer):
        instance = serializer.save()

        # Sardor, Zoir, Jasur postlarini topib, yangilash
        for post_model in [SardorPost, ZoirPost, JasurPost]:
            posts = post_model.objects.all()
            for post in posts:
                post.firstName = instance.firstName
                post.lastName = instance.lastName
                post.birthDate = instance.birthDate
                post.address = instance.address
                post.appointmentDate = instance.appointmentDate
                post.appointmentTime = instance.appointmentTime
                post.doctor = instance.doctor
                post.price = instance.price
                post.givenPrice = instance.givenPrice
                post.tel = instance.tel
                post.description = instance.description
                post.save()

    def perform_destroy(self, instance):
        # Barcha Sardor, Zoir va Jasur postlarini o‘chirish
        SardorPost.objects.all().delete()
        ZoirPost.objects.all().delete()
        JasurPost.objects.all().delete()

        instance.delete()
