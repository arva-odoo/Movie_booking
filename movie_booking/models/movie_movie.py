# -*- coding: utf-8 -*-
from odoo import models,fields

class movie_movie(models.Model):
    _name = 'movie.movie'
    _description = 'movie booking management'

    name = fields.Char('Movie name',required=True)
    release_date = fields.Date('release date')
    movie_language = fields.Char('Movie language',required=True)
    date_from = fields.Date('From')
    date_to = fields.Date('To')
    show_duration = fields.Float(string='show duration')
    image = fields.Image('image')
    seating_template = fields.Many2one('movie.show.template',string="seating_template")
    show = fields.Float(string='show')
