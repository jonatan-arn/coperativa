# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime,re
from odoo.exceptions import ValidationError

class campana_model(models.Model):
    _name = 'coperativa.campana_model'
    _description = 'modulo de campañas'
    
    fecha = fields.Datetime(string="Fecha inicio de la campaña",index=True,required=True,default=lambda self:datetime.datetime.now())
    campana = fields.Integer(string="Fecha de la campaña",index=True,required=True,compute="calc_año")
    socio = fields.Many2one("coperativa.socio_model",required=True)
    producto = fields.Many2one("coperativa.producto_model",required=True)
    kilo = fields.Float(String = "Cantidad",index= True,required=True,default=0)
    active = fields.Boolean(readonly=True,default=True)
    

    def saldo(self):
        listaSocios = self.search([("active","=","True")])
        for s in listaSocios:
            s.producto.kilos+=s.kilo
            s.socio.saldo+=s.kilo*s.producto.precio
            s.active=False

    
            

    def calc_año(self):
        
        hoy = datetime.date.today()
        self.campana = int(hoy.year)

    @api.constrains('kilo')
    def validate_kilo(self):
        if not self.comprovar_kilo():
            raise ValidationError("Error la cantidad no puede ser menor de 0")

    def comprovar_kilo(self):
        if self.kilo<0:
            return False
        
        return True
