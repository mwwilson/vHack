from pyramid.security import Allow, Authenticated, remember, forget
from pyramid.view import view_config
from pyramid.response import Response


@view_config(route_name='home', renderer='templates/mytemplate.pt',
             permission='view')
def my_view(request):
    return {'project': 'onboarding'}

@view_config(route_name='application', renderer='templates/application.pt')
def application(request):
    return {'project': 'onboarding'}

@view_config(route_name='login')
def login(request):
    #userid = request.params.get('userid')
    userid = 'Bob'
    headers = remember(request, userid)
    return Response(
        'Logged in as %s' % userid,
        headers=headers
        )

@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    return Response(
        'Logged out',
        headers=headers
        )
