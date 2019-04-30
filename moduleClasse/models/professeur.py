'''
Created on 30 avr. 2019

@author: rt
'''

from odoo import models, fields, api


class professeur(models.Model):
     _name = 'res.partner'
     _inherit= 'res.partner'
     
     classe_ids = fields.Many2many('iutclasse', string='classes du professeur')

