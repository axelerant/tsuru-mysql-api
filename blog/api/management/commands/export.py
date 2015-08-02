# -*- coding: utf-8 -*-

# Copyright 2013 mysqlapi authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from django.core.management.base import NoArgsCommand

from blog.api.database import export
from blog.api.management.commands import s3


class Command(NoArgsCommand):

    can_import_settings = True

    def handle_noargs(self, **options):
        data = export()
        self.send_data(data)
        return u"Successfully exported!"

    def send_data(self, data):
        s3.store_data(data)
