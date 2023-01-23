# -*- coding: utf-8 -*-
from odoo import models,fields

class movie_type(models.Model):
    _name = 'movie.type'
    _description = 'define show type'

    name = fields.Char("name")
    movie_ids = fields.Many2many('movie.movie')
    color = fields.Integer('color')