# -*- coding: utf-8 -*-
from odoo import models,fields

class movie_type(models.Model):
    _name = 'movie.type'
    _description = 'define show type'

    name = fields.Char("name")
    color = fields.Integer('color')