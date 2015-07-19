from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'onboarding'}

@view_config(route_name='application', renderer='templates/application.pt')
def application(request):
    return {'project': 'onboarding'}
