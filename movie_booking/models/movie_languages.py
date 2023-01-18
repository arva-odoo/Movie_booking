# -*- coding: utf-8 -*-
from odoo import models,fields

class MovieLanguages(models.Model):
    _name = 'movie.languages'
    _description = 'define show languages'

    name = fields.Char("name")
    movie_ids = fields.One2many('movie.movie','movie_language_id',string="movie Type")