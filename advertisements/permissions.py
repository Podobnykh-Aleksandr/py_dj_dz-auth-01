from pprint import pprint

from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        ''' Проверяет права на конкретный объект '''
        pprint(request)
        if request.method == 'GET':
            return True
        return request.user == obj.creator
