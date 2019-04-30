'''
Created on 30 avr. 2019

@author: rt
'''

from odoo import models, fields, api


class cours(models.Model):
     _name = 'iutcours'

     name = fields.Char("nom", required=True)

     agenda_ids = fields.One2many('iutagenda', 'cours_id', 'agendas')
   