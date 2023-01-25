# -*- coding: utf-8 -*-
from odoo import models,fields,api

class movie_booking(models.Model):
    _name = 'movie.booking'
    _inherits = {'movie.show':'movie_show_id'}
    _description = 'movie booking management'

    # show_ids = fields.One2many('movie.show','movie_booking_id',string="movie Booking")
    movie_show_id = fields.Many2one('movie.show',required=True)
    customer = fields.Char('customer')