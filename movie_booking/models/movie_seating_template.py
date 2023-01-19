# -*- coding: utf-8 -*-
from odoo import models,fields

class movie_seating_template(models.Model):
    _name = 'movie.seating.template'
    _description = 'show movie seating template'

    name = fields.Char('Name',required=True)
    show_time = fields.Float('show_time')
    ticket_type = fields.Char('Ticket type')
    price = fields.Integer('Price',required=True)
    # max_seat_in_one_row = fields.Integer('Total row')
    
