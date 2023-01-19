# -*- coding: utf-8 -*-
from odoo import models,fields,api

class Movie_seat_arrangement(models.Model):
    _name = 'movie.seat.arrangement'
    _inherits = {'movie.seating.template':'seat_template_id'}
    _description = 'movie booking management'

    seat_template_id = fields.Many2one('movie.seating.template')
    # screen = fields.Char('screen')
    # show_time = fields.Float('show time')
    # ticket_type = fields.Char('ticket type')
    max_seat_in_one_row = fields.Integer('max seat in one row')
    