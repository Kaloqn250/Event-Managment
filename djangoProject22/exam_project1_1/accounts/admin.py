# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import Group
#
# from .models import CustomUser
#
# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     fieldsets = UserAdmin.fieldsets
#
#     list_display = ('username', 'email', 'role', 'is_staff', 'is_superuser')
#     list_filter = ('role', 'is_staff', 'is_superuser')
#
#     def save_model(self, request, obj, form, change):
#         super().save_model(request, obj, form, change)
#         if obj.role == 'superuser':
#             obj.groups.set([Group.objects.get(name='Superuser')])
#             obj.is_superuser = True
#         elif obj.role == 'staff':
#             obj.groups.set([Group.objects.get(name='Staff')])
#             obj.is_staff = True
#         else:
#             obj.groups.clear()
#             obj.is_superuser = False
#             obj.is_staff = False
#         obj.save()