
from rest_framework.views import APIView
from rest_framework.response import Response
import casbin

class CheckPermissionView(APIView):
    def get(self, request):
        user = request.query_params.get('user')
        resource = request.query_params.get('resource')
        action = request.query_params.get('action')

        enforcer = casbin.Enforcer('path/to/model.conf', 'path/to/policy.csv')
        has_permission = enforcer.enforce(user, resource, action)

        return Response({"allowed": has_permission})