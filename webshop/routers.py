"""Defines a custom router for adding viewsets and function based view together to the root api view
"""
from collections import OrderedDict
from importlib import import_module

from rest_framework import routers


class MyDefaultRouter(routers.DefaultRouter):
    """Overwrites the :class:`DefaultRouter <rest_framework.routers.DefaultRouter>` so the Root API
    view can be extended with function based views as well.
    """

    def get_api_root_dict(self):
        """Returns the viewset based dynamically generated routes.
        """
        api_root_dict = OrderedDict()
        list_name = self.routes[0].name
        for prefix, _, basename in self.registry:
            api_root_dict[prefix] = list_name.format(basename=basename)
        return api_root_dict

    def get_api_root_view(self, api_urls=None):
        """Returns the Root API view"""
        api_root_dict = self.get_api_root_dict()
        return self.APIRootView.as_view(api_root_dict=api_root_dict)


class APIRouter(MyDefaultRouter):
    """API Router which can consume viewsets and function based views as well.
    """
    #: Registry of function based views
    extra_registry = []

    def register_view(self, *routes):
        """Registers function based views for the root api view.
        .. codeblock:: python
            from routers import APIRouter
            from myapp import urls as my_urls
            api_router = APIRouter()
            # Use the string representatation of your url conf module
            api_router.register_view('myapp.urls')
            # or register all the views
            api_router.register_view(*my_urls.url_patterns)
        :param routes: Any number of :func:`path <django.urls.path>` objects or a URL configuration
                       module.
        """
        if len(routes) == 1 and isinstance(routes[0], str):
            urlconf_module = import_module(routes[0])
            routes = getattr(urlconf_module, 'urlpatterns', urlconf_module)

        for route in routes:
            if route.name not in [view.name for view in self.extra_registry]:
                self.extra_registry.append(route)

    def get_api_root_dict(self):
        """Returns the root api view extendedwith function based views.
        """
        api_root_dict = super().get_api_root_dict()

        for route in self.extra_registry:
            api_root_dict[route.name] = route.name

        return api_root_dict

    def get_urls(self):
        """Returns the urls generated from viewsets and the extra function based views as well.
        """
        urls = super().get_urls()

        for route in self.extra_registry:
            urls.append(route)

        return urls
