# -*- coding: utf-8 -*-
from odoo import models,fields

class movie_movie(models.Model):
    _name = 'movie.movie'
    _description = 'movie booking management'

    name = fields.Char('Movie name',required=True)
    release_date = fields.Date('release date')
    movie_language = fields.Char('Movie language',required=True)
    start_date = fields.Date('start date')
    end_date = fields.Date('End date')
    
