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
    # movie_language_id = fields.Many2one(related="movie_id.movie_language_id",store=True)

    def action_screen(self):
        # for rec in self:
        #     self.env['movie.seating.template'].create({
        #         'name' : rec.seating_template
        #     })
        return{
            'res_model':'movie.seating.template',
            'type':'ir.actions.act_window',
            'view_mode':'form',
            'view_type':'form',
            'view_id':self.env.ref("movie_booking.template_form_view").id,
            # 'domain':[('seating_template', '=', active_id)],
            'target':'self',
            # 'domain':[('seating_template', '=', active_id)]
        }