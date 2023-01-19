# -*- coding: utf-8 -*-
from odoo import models,fields,api

class movie_movie(models.Model):
    _name = 'movie.movie'
    _description = 'movie booking management'

    movie_language_id = fields.Many2one('movie.languages',string="movie languages")
    movie_type_ids = fields.Many2many('movie.type',string='movie type')
    name = fields.Char('Movie name',required=True)
    release_date = fields.Date('release date')
    # movie_language = fields.Char('Movie language')
    date_from = fields.Date('From')
    date_to = fields.Date('To')
    show_duration = fields.Float(string='show duration')
    image = fields.Image('image')
    # seating_template = fields.Many2one('movie.seating.template',string="seating_template")
    show_ids = fields.One2many('movie.show','movie_id',string="movie shows")
    show_count = fields.Integer('show count',compute='_compute_show_count',default=0)

    @api.depends('show_ids','show_count')
    def _compute_show_count(self):
        for record in self:
            record.show_count = len(record.show_ids)
