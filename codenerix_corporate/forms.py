# -*- coding: utf-8 -*-
#
# django-codenerix-corporate
#
# Codenerix GNU
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

from django.utils.translation import gettext_lazy as _
from codenerix.forms import GenModelForm
from codenerix_corporate.models import CorporateImage


class CorporateImageForm(GenModelForm):
    class Meta:
        model = CorporateImage
        exclude = ['name_file_sign', 'name_file_seal', 'name_file_logo', ]

    def __groups__(self):
        g = [
            (
                _('Details'), 12,
                ['business_name', 6],
                ['nid', 4],
                ['public', 2],
                ['phone', 6],
                ['email', 6],
                ['digital_sign', 4],
                ['company_seal', 4],
                ['company_logo', 4],
            ),
            (
                _('Address'), 12,
                ['country', 4],
                ['region', 4],
                ['province', 4],
                ['city', 6],
                ['town', 6],
                ['address', 8],
                ['zipcode', 4],
            )
        ]
        return g

    @staticmethod
    def __groups_details__():
        g = [
            (
                _('Details'), 12,
                ['business_name', 6],
                ['nid', 4],
                ['public', 2],
                ['phone', 6],
                ['email', 6],
                ['digital_sign', 4],
                ['company_seal', 4],
                ['company_logo', 4],
            ),
            (
                _('Address'), 12,
                ['country', 4],
                ['region', 4],
                ['province', 4],
                ['city', 6],
                ['town', 6],
                ['address', 8],
                ['zipcode', 4],
            )
        ]
        return g
