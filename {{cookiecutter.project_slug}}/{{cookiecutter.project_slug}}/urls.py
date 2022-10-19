from api.urls import router

from {{ cookiecutter.project_slug }}.views import (
    landing_page, 
    CustomSearch,
    TransferView,
    SearchTransferView,
)

from django.urls import path, include, reverse
from django.shortcuts import redirect
from globus_portal_framework.urls import register_custom_index

register_custom_index('fema', ['fema'])

urlpatterns = [
    # Provides the basic search portal
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
    
    # We only want to show a single index with no main landing page,
    # so redirect home requests to the fema search-about page.
    path("", lambda r: redirect(reverse('search-about', args=['fema'])), name="landing-page"),
    
    path("<fema:index>", CustomSearch.as_view(), name="search"),
    path("<fema:index>/search-transfer", SearchTransferView.as_view(),
         name="search-transfer"),
    path("transfer/", TransferView.as_view(), name="transfer"),
    
    path("", include("globus_portal_framework.urls")),
    path("", include("social_django.urls", namespace="social")),
]
