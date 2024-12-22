from pyramid.view import view_config


@view_config(route_name='outfit_display', renderer='outfit_generator:templates/outfit_displayer.jinja2')
def display(request):
    return {'greeting': 'Welcome, Aryanna!'}
