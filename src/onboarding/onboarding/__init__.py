from pyramid.response import Response
from pyramid.config import Configurator
from pyramid.security import Allow, Authenticated, remember, forget
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

class Resource(object):
    def __init__(self, name='', acl=None,
                 parent=None):
        self.children = {}
        self.__name__ = name
        self.__parent__ = parent
        if acl is not None:
            self.__acl__ = acl

    def add_subresource(self, name, acl=None):
        self.children[name] = Resource(
            name, acl=acl, parent=self
            )

    def __getitem__(self, name):
        return self.children[name]

    def __repr__(self):
        return '<Resource named %r at %s>' % (
            self.__name__, id(self)
            )

def root_factory(request):
    root = Resource(
        '',
        acl=[(Allow, Authenticated, 'view'),
             (Allow, 'admin', 'assign')]
        )
    return root

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    authn_policy = AuthTktAuthenticationPolicy('soseekrit')
    authz_policy = ACLAuthorizationPolicy()

    settings['users'] = {'marshall' : {'password' : 'viasat', 
                                       'tasks'    : {'Application' : 'complete',
                                                     'Training'    : 'incomplete'
                                                    }
                                      },
                         'Ian'      : {'password' : 'aese',
                                       'tasks'    : {'Application' : 'incomplete'
                                                    }
                                      },
                         'admin'    : {'password' : 'admin',
                                       'tasks'    : {}
                                      }
                            }
    config = Configurator(settings=settings,
        root_factory=root_factory,
        authentication_policy=authn_policy,
        authorization_policy=authz_policy)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=0)
    config.add_route('home', '/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('admin', '/admin')
    config.add_route('signup', '/signup')
    config.add_route('germantown', '/germantown')
    config.add_route('login_success', '/login_success')
    config.add_route('application', '/application')
    config.add_route('offer_letter', '/offer_letter')
    config.add_route('offer_letter_task', '/offer_letter_task')
    config.add_route('get_tasks', '/get_tasks')
    config.add_route('add_task', '/add_task/{user}/{task}')
    config.add_route('get_users_and_tasks', '/get_users_and_tasks')
    config.add_route('submit', '/submit/{taskname}')
    config.add_route('training', '/training')
    config.scan()
    return config.make_wsgi_app()
