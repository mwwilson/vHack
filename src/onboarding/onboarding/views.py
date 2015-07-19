from pyramid.security import Allow, Authenticated, remember, forget
from pyramid.view import view_config, forbidden_view_config
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
    return {'project': 'onboarding'}

@view_config(route_name='admin', renderer='templates/admin.pt',
             permission='assign')
def admin(request):
    return {'Project': 'Assignment Page'}

@view_config(route_name='application', renderer='templates/application.pt')
def application(request):
    return {'project': 'onboarding'}

@forbidden_view_config(renderer='templates/login.pt')
def forbidden(request):
    return {"You must log in to see that" : "Young Padawan"}

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


@view_config(route_name='germantown', renderer='templates/germantown.pt')
def germantown(request):
    return {'project' : 'onboarding'}

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

@view_config(route_name='submit', renderer="json")
def submit(request):
    task_name = request.matchdict['taskname']
    request.registry._get_settings()['users'][request.cookies['username']][task_name] = "complete"
    return {'response': 'completed'}

@view_config(route_name='get_tasks', renderer="json")
def get_tasks(request):
    user_name = request.cookies['username']
    return {'response': request.registry._get_settings()['users'][user_name]['tasks']}

@view_config(route_name='get_users_and_tasks', renderer='json', permission='assign')
def get_users_and_tasks(request):
    users = request.registry._get_settings()['users']
    return users

@view_config(route_name='add_task', renderer="json", permission="assign")
def add_task(request):
    try:
        user = request.matchdict['user']
        task = request.matchdict['task']
        request.registry._get_settings()['users'][user]['tasks'][task] = 'incomplete'
        return Response("Task %s added to user %s" % (task, user))
    except:
        return Response("Error. Task not added")
