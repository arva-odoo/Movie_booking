# -*- coding: utf-8 -*-
from odoo import models,fields

class movie_show(models.Model):
    _name = 'movie.show'
    _inherits = {'movie.movie':'movie_id'}
    _description = 'movie booking management'

    show = fields.Float(string='Show')
    movie_id = fields.Many2one('movie.movie',required=True)