'''
Created on 30 avr. 2019

@author: rt
'''

from odoo import models, fields, api


class classe(models.Model):
     _name = 'iutclasse'

     name = fields.Char("nom", required=True)
     level = fields.Selection([('seconde', 'Seconde'), ('première', 'Première'), ('terminale', 'Terminale')], string='niveau')
     nb_etudiant = fields.Integer("nombre d'étudiants")
     
     prof_ids = fields.Many2many('res.partner', string='professeur utilisant la classe')
     etudiant_ids = fields.One2many('iutetudiant', 'classe_id', string='étudiants')
     agenda_ids = fields.One2many('iutagenda', 'class_id', 'agendas')

   
     _sql_constraints = [
         ('nom_unique', 'unique (name)', 'copies pas mon style mec ')
    ]