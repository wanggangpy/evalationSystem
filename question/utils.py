from django.contrib import messages
from django.shortcuts import redirect


class MessageMixin:

    error_url = ''

    def success_msg(self):
        return NotImplemented

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_msg)
        return super(MessageMixin, self).delete(request, *args, **kwargs)

    def form_invalid(self, form):

        error_msg = [key[0]['message'] for key in list(form.errors.get_json_data().values())][0]
        messages.error(self.request, error_msg)

        if not self.error_url:
            self.error_url = self.request.session['login_from']

        return redirect(self.error_url)

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(MessageMixin, self).form_valid(form)