from django.views import View
from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class IsSelfOrAdminProfilePermission(BasePermission):
    message = "You do not have permission to perform this action."

    allowed_user_fields = {"first_name", "last_name", "phone"}
    forbidden_user_fields = {"role", "is_staff", "is_superuser", "deleted"}

    def has_permission(self, request: Request, view: View) -> bool:
        user = request.user

        if not user or not user.is_authenticated:
            self.message = "Authentication credentials were not provided."
            return False

        if user.role == "admin":
            return True

        if view.action in {"list", "create", "destroy"}:
            self.message = "You do not have permission to perform this action."
            return False

        return True

    def has_object_permission(self, request: Request, view: View, obj) -> bool:
        user = request.user

        if user.role == "admin":
            return True

        if view.action in {"retrieve", "get_me"}:
            if obj.pk != user.pk:
                self.message = "You can view only your own profile."
                return False
            return True

        if view.action in {"update", "partial_update"}:
            if obj.pk != user.pk:
                self.message = "You can update only your own profile."
                return False

            incoming_fields = set(request.data.keys())

            forbidden_fields_in_request = incoming_fields & self.forbidden_user_fields
            if forbidden_fields_in_request:
                self.message = (
                    "You cannot modify the following fields: "
                    f"{', '.join(sorted(forbidden_fields_in_request))}."
                )
                return False

            not_allowed_fields = incoming_fields - self.allowed_user_fields
            if not_allowed_fields:
                self.message = (
                    "You can change only the following fields: "
                    "first_name, last_name, phone. "
                    "Invalid fields: "
                    f"{', '.join(sorted(not_allowed_fields))}."
                )
                return False

            return True

        self.message = "You do not have permission to perform this action."
        return False
