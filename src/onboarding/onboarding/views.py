from pyramid.security import Allow, Authenticated, remember, forget
from pyramid.view import view_config
from pyramid.response import Response

def verify(users, creds):
    try:
        if creds['username'] in users:
            if creds['password'] == users[creds['username']]['password']:
                return creds['username']
    except:
        pass
    return None

@view_config(route_name='home', renderer='templates/mytemplate.pt',
             permission='view')
def my_view(request):
    import pdb; pdb.set_trace()
    return {'project': 'onboarding'}

@view_config(route_name='application', renderer='templates/application.pt')
def application(request):
    return {'project': 'onboarding'}

@view_config(route_name='login', renderer='templates/login.pt')
def login(request):
    return {'login' : 'page'}

@view_config(route_name='signup')
def signup(request):
    creds = request.json_body
    users = request.registry._get_settings()['users']
    users[creds['username']] = {'password':creds['password']}
    userid = creds['username']
    headers = remember(request, userid)
    toReturn = Response(
        'Account for User %s Created' % userid,
        headers=headers
        )
    toReturn.set_cookie('username', userid)
    return toReturn

@view_config(route_name='login_success')
def login_success(request):
    creds = request.json_body
    userid = verify(request.registry._get_settings()['users'], creds)
    if userid:
        headers = remember(request, userid)
        toReturn = Response(
            'Logged in as User %s' % userid,
            headers=headers
            )
        toReturn.set_cookie('username', userid)
        return toReturn
    else:
        return Response('Login Attempt Failed for User %s' % (creds['username']))

@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    return Response(
        'Logged out',
        headers=headers
        )
