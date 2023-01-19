# -*- coding: utf-8 -*-
from odoo import models,fields

class movie_show(models.Model):
    _name = 'movie.show'
    _inherits = {'movie.movie':'movie_id'}
    _description = 'movie booking management'

    show = fields.Float(string='Show')
    movie_id = fields.Many2one('movie.movie',required=True)
    seating_template = fields.Many2one('movie.seating.template',string="seating_template")
    # movie_language_id = fields.Many2one(related="movie_id.movie_language_id",store=True)