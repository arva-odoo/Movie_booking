# -*- coding: utf-8 -*-
from odoo import models,fields,api

class MovieLanguages(models.Model):
    _name = 'movie.languages'
    _description = 'define show languages'

    name = fields.Char("name")
    movie_ids = fields.One2many('movie.movie','movie_language_id',string="movie Type")
    count_movie = fields.Integer('total movie',compute='_compute_total_movie')

    @api.depends('movie_ids','count_movie')
    def _compute_total_movie(self):
        for record in self:
            record.count_movie = len(record.movie_ids)