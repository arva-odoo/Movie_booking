# -*- coding: utf-8 -*-
from odoo import models,fields

class movie_show(models.Model):
    _name = 'movie.show'
    _inherits = {'movie.movie':'movie_id'}
    _description = 'movie booking management'
    _rec_name = "show"

    show = fields.Float(string='Show')
    movie_id = fields.Many2one('movie.movie',required=True)
    seating_template = fields.Many2one('movie.seating.template',string="seating_template")
    # movie_booking_id = fields.Many2one('movie.booking',string="movie booking")
    # movie_language_id = fields.Many2one(related="movie_id.movie_language_id",store=True)

    def action_screen(self):
        return{
            'res_model':'movie.seating.template',
            'type':'ir.actions.act_window',
            'view_mode':'form',
            'view_type':'form',
            'res_id' : self.env['movie.seating.template'].search([('name','=',self.seating_template.name)]).id,
            # 'domain':[('seating_template', '=', active_id)],
            'target':'current',
            # 'flags':{mode:'readonly'},
        }