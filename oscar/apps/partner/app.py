from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from oscar.core.application import Application
from oscar.core.loading import get_class
from . import views


class PartnerApplication(Application):
    name = 'partner'
    # summary_view = get_class('basket.views', 'BasketView')
    # saved_view = get_class('basket.views', 'SavedView')
    # add_view = get_class('partner.views', 'MyFormView')
    # add_voucher_view = get_class('basket.views', 'VoucherAddView')
    # remove_voucher_view = get_class('basket.views', 'VoucherRemoveView')

    def get_urls(self):
        urls = [
            # url(r'^$', self.summary_view.as_view(), name='summary'),
            url(r'^addInfo/(?P<pk>\d+)/$', views.form_view, name='addInfo'),
            # url(r'^vouchers/add/$', self.add_voucher_view.as_view(),
            #     name='vouchers-add'),
            # url(r'^vouchers/(?P<pk>\d+)/remove/$',
            #     self.remove_voucher_view.as_view(), name='vouchers-remove'),
            # url(r'^saved/$', login_required(self.saved_view.as_view()),
            #     name='saved'),
        ]
        return self.post_process_urls(urls)


application = PartnerApplication()