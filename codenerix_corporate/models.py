# -*- coding: utf-8 -*-
#
# django-codenerix-corporate
#
# Copyright 2017 Centrologic Computational Logistic Center S.L.
#
# Project URL : http://www.codenerix.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.db import models, transaction
from django.utils.translation import ugettext_lazy as _

from codenerix.models import CodenerixModel
from codenerix.exceptions import CodenerixException
from codenerix.lib.helpers import upload_path
from codenerix.fields import ImageAngularField


class CorporateImage(CodenerixModel):

    nid = models.CharField(_("NID"), max_length=20, blank=True)
    business_name = models.CharField(_("Business name"), max_length=254, blank=True, null=True)
    digital_sign = ImageAngularField(_("Digital sign"), upload_to=upload_path, max_length=200, blank=True, null=True)
    name_file_sign = models.CharField(_("Name file digital sign"), max_length=254, blank=True, null=True)
    company_seal = ImageAngularField(_("Company seal"), upload_to=upload_path, max_length=200, blank=True, null=True)
    name_file_seal = models.CharField(_("Name file company seal"), max_length=254, blank=True, null=True)
    company_logo = ImageAngularField(_("Company logo"), upload_to=upload_path, max_length=200, blank=True, null=True)
    name_file_logo = models.CharField(_("Name file company logo"), max_length=254, blank=True, null=True)
    public = models.BooleanField(_("Public"), default=False)
    address = models.CharField(_("Address"), max_length=254, blank=True, null=True)
    zipcode = models.CharField(_("Zipcode"), max_length=10, blank=True, null=True)
    province = models.CharField(_("Province"), max_length=254, blank=True, null=True)
    city = models.CharField(_("City"), max_length=254, blank=True, null=True)
    phone = models.CharField(_("Phone"), max_length=60, blank=True, null=True)
    email = models.EmailField(_("Email"), max_length=60, blank=True, null=True)

    def __unicode__(self):
        return self.__str__()

    def __str__(self):
        return u"{}".format(self.business_name)

    def __fields__(self, info):
        fields = []
        fields.append(('nid', _('NID')))
        fields.append(('business_name', _('Business name')))
        fields.append(('address', _('Address')))
        fields.append(('zipcode', _('Zipcode')))
        fields.append(('province', _('Province')))
        fields.append(('city', _('City')))
        fields.append(('phone', _('Phone')))
        fields.append(('email', _('Email')))
        fields.append(('public', _('Public')))
        fields.append(('updated', _('Last Update')))
        return fields

    def save(self, *args, **kwards):
        """
        Siempre debe haber un registro marcado como público
        There should always be a record marked as public
        """
        try:
            with transaction.atomic():
                if self.public:
                    CorporateImage.objects.exclude(pk=self.pk).update(public=False)
                elif not CorporateImage.objects.exclude(pk=self.pk).filter(public=True).exists():
                    self.public = True

                return super(CorporateImage, self).save(*args, **kwards)
        except CodenerixException:
            return super(CorporateImage, self).save(*args, **kwards)
