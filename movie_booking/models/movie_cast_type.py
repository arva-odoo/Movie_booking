# -*- coding: utf-8 -*-
from odoo import models,fields

class movie_cast(models.Model):
    _name = 'movie.cast.type'
    _description = 'define movie cast type'

    name = fields.Char("name")