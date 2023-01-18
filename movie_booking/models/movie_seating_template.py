# -*- coding: utf-8 -*-
from odoo import models,fields

class movie_seating_template(models.Model):
    _name = 'movie.seating.template'
    _description = 'show movie seating template'

    name = fields.Char('Template',required=True)
    ticket_type = fields.Char('Ticket type')
    price = fields.Integer('Price',required=True)
    total_row = fields.Integer('Total row')
    
