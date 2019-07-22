# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status


class HelloApiView(APIView):
    """ Test api view. """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Returns a list of APIView sets. """

        an_apiview = [
            'Uses http methods as functions get, post, put, delete',
            'it is similar to a traditional django view',
            'gives you the most control of your logic',
            'is mapped manually to urls'

        ]

        return Response({"message": "hello", "an_apiview": an_apiview})

    def post(self, request):
        """ Create a hello message with a name. """

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello {0}".format(name)

            return Response({"message": message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ Handles object updates. """

        return Response({"method": "put"})

    def patch(self, request, pk=None):
        """ Only updates specific fields provided in the request"""

        return Response({"method": "patch"})

    def delete(self, request, pk=None):
        """ Deletes an object """

        return Response({"method": "Delete"})
