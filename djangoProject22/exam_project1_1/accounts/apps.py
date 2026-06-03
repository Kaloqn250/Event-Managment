from django.apps import AppConfig



class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'exam_project1_1.accounts'

    def ready(self):
        import exam_project1_1.accounts.signals
        from django.contrib.auth.models import Group, Permission
        from django.contrib.contenttypes.models import ContentType
        from django.db.models.signals import post_migrate

        def create_groups(sender, **kwargs):
            # Superuser Group
            superuser_group, _ = Group.objects.get_or_create(name='Superuser')
            # Assign all permissions to Superuser
            superuser_group.permissions.set(Permission.objects.all())

            # Staff Group
            staff_group, _ = Group.objects.get_or_create(name='Staff')
            # Assign limited permissions to Staff
            staff_permissions = Permission.objects.filter(
                content_type__app_label='myapp',  # Replace with your app name
                codename__in=['add_event', 'change_event', 'view_event']
            )
            staff_group.permissions.set(staff_permissions)

        post_migrate.connect(create_groups, sender=self)