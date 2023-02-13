from actstream import action, registry

from das_demo.user.models import User
from actstream.models import user_stream, Action

# User.objects.create_user(username='tony', password='123123', email='a@a.com')
# User.objects.create_user(username='mary', password='123123', email='b@a.com')
#
u1 = User.objects.get(username='tony')
u2 = User.objects.get(username='mary')

try:
    registry.check(u1.__class__)
    print('register model working ?')
except Exception as e:
    print(e)

# action.send(u1, verb='joined actstream')
# action.send(u1, verb='say hello', target=u2)

print('stream working ', user_stream(u1, with_user_activity=True).count())

try:
    print(Action.objects.filter(actor=u1))
except Exception as e:
    print(e)
# ERROR django.core.exceptions.FieldError: Field 'actor' does not generate an automatic reverse relation and therefore cannot be used for reverse querying. If it is a GenericForeignKey, consider adding a GenericRelation.
