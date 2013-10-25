from street_faces.subscription.forms import subscription_form


class FormMiddleware(object):
    def process_request(self, request):
        request.subscription_form = subscription_form
