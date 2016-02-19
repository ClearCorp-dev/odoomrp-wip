# -*- coding: utf-8 -*-
# © 2016 Oihane Crucelaegui - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from . import models


def populate_unrevisioned_name(cr, registry):
    cr.execute('UPDATE qc_test '
               'SET unrevisioned_name = name '
               'WHERE unrevisioned_name is NULL')
