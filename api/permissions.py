from rest_framework.permissions import BasePermission

class CustomPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(f"User is {requwst.user}")
        print(f"Obj is{obj}")
        print(f"View is {view}")
        return True
