from django.test import TestCase
from django.urls import path, reverse
from django.http import HttpResponse
from django.test import override_settings, modify_settings


urlpatterns = [
    path("", lambda request: HttpResponse("<body>OK</body>"), name="index")
]


@modify_settings(
    MIDDLEWARE={
        "append": "version_control.middleware.VersionControlMiddleware"
    },
    INSTALLED_APPS={
        "append": "version_control"
    },
)
@override_settings(
    ROOT_URLCONF="version_control.tests.test_middleware",
    VERSION_CONTROL_BACKEND="version_control.backends.dummy.DummyVersionControlBackend"  # noqa
)
class VersionControlMiddlewareTests(TestCase):
    def test_should_add_version_control_bar_to_response(self):
        url = reverse("index")

        response = self.client.get(url)
        response_content = response.content.decode()

        self.assertIn('<div id="version_control_panel">dummy_backend',
                      response_content)
