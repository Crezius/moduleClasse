'''
Created on 30 avr. 2019

@author: rt
'''


from odoo import models, fields, api


class etudiant(models.Model):
     _name = 'iutetudiant'

     firstname = fields.Char("prenom", required=True)
     lastname = fields.Char("nom", required=True)
     birthdate = fields.Date("date de naissance")
     age = fields.Integer("age")

     classe_id = fields.Many2one('iutclasse', string='étudiants')
