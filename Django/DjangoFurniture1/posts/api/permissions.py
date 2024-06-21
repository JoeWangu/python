from rest_framework.permissions import BasePermission,SAFE_METHODS


class isOwnerOrReadOnly(BasePermission):
    message = 'you must be the owner of this object.'
    my_safe_method = ['GET', 'PUT']
    def has_permission(self, request, view):
        if request.method in self.my_safe_method:
            return True
        return False


    def has_object_permission(self,request,view,obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user









# orginal method. works well
# class isOwnerOrReadOnly(BasePermission):
#     message = 'you must be the owner of this object.'
#     def has_object_permission(self,request,view,obj):
#         my_safe_method = ['PUT']
#         if request.method in my_safe_method:
#             return True
#         return obj.user == request.user