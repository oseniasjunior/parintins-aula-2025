from django.db.models import Func, F, IntegerField


class Age(Func):
    function = "DATE_PART"
    template = "%(function)s('year', AGE(%(expressions)s))"
    output_field = IntegerField()
