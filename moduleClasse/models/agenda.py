'''
Created on 30 avr. 2019

@author: rt
'''

from odoo import models, fields, api


class agenda(models.Model):
     _name = 'iutagenda'

     date_start = fields.Date("date de début", required=True)
     date_stop = fields.Date("date de fin", required=True)
     room = fields.Char("salle de classe en cours")
   
     class_id = fields.Many2one('iutclasse', string='classe')
     cours_id = fields.Many2one('iutcours', string='cours')

   