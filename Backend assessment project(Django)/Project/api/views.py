from django.shortcuts import render

# Create your views here.
# from .models import Profile
# from . import serializers
# from rest_framework import generics, status
# from rest_framework.response import Response


# class ProfileListView(generics.ListAPIView):
#     queryset = profile.objects.all()
#     serializers_class = serializers.ProfileSerializer

#     #  def List(self, request, *args, **kwargs):
#     #     super(ProfileListView, self).list(request, args, kwargs)
#     #     response = {
#     #         "status_code": status.HTTP_200_OK,
#     #         "message": "Successfully created",
#     #         "result": request.data}

#     #     return Response(response)
    

# class ProfileCreateView(generics.CreateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = serializers.ProfileSerializer

#     def create(self, request, *args, **kwargs):
#         super(ProfileCreateView, self).create(request, args, kwargs)
#         response = {
#             "status_code": status.HTTP_200_OK,
#             "message": "Successfully created",
#             "result": request.data}

#         return Response(response)

# class ProfileDetailsView(generics.RetrieveAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = serializers.PostSerializer

#     def retrieve(self, request, *args, **kwargs):
#         super(ProfileDetailView, self).retrieve(request, args, kwargs)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
 
#         data = serializer.data
#         response = {"status_code": status.HTTP_200_OK,
#                     "message": "Successfully retrieved",
#                     "result": data}
#         return Response(response)
    
# class ProfileDetailsView(generics.UpdateAPIView):
#     def patch(self, request, *args, **kwargs):
#         super(ProfileDetailView, self).patch(request, args, kwargs)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         data = serializer.data
#         response = {"status_code": status.HTTP_200_OK,
#                     "message": "Successfully updated",
#                     "result": data}
#         return Response(response)

# class ProfileDetailsView(generics.DestroyAPIView):
#     def delete(self, request, *args, **kwargs):
#         super(ProfileDetailView, self).delete(request, args, kwargs)
#         response = {"status_code": status.HTTP_200_OK,
#                     "message": "Successfully deleted"}
#         return Response(response)


