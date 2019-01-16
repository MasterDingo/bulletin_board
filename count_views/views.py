from django.shortcuts import render

from .models import Visitor

import json

# Create your views here.

COOKIE_KEY = "bulletin_counter"


class CountableViewMixin:
    def get(self, request, *args, **kwargs):
        cookies = request.COOKIES
        visitor_guid = None
        pk = kwargs['pk']
        self.increment_view_count = False
        if COOKIE_KEY in cookies:
            visitor_guid = cookies[COOKIE_KEY]
        visitor, created = Visitor.objects.get_or_create(id=visitor_guid)
        if created:
            seen_ids = []
        else:
            seen_ids = json.loads(visitor.seen_ids)
        if pk not in seen_ids:
            self.increment_view_count = True
            seen_ids.append(pk)
        visitor.seen_ids = json.dumps(seen_ids)
        visitor.save()

        response = super().get(request, *args, **kwargs)
        response.set_cookie(COOKIE_KEY, visitor.id, 10*365*24*60*60)
        return response

    def get_object(self, *args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        if self.increment_view_count:
            obj.views_count += 1
            obj.save()
        return obj
