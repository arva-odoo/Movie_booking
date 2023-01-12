# -*- coding: utf-8 -*-
from odoo import models,fields

class movie_cast(models.Model):
    _name = 'show.type'
    _description = 'define show type'

    name = fields.Char("name")