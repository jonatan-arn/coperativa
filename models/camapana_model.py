# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime,re
from odoo.exceptions import ValidationError

class campana_model(models.Model):
    _name = 'coperativa.campana_model'
    _description = 'modulo de campañas'
    
    fecha = fields.Date(string="Fecha inicio de la campaña",index=True,required=True,default=fields.date.today())
    campana = fields.Integer(string="Fecha de la campaña",index=True,required=True,compute="calc_año")
    socio = fields.Many2one("coperativa.socio_model")
    producto = fields.Many2one("coperativa.producto_model")
    kilo = fields.Float(String = "Cantidad",index= True,required=True,default=0)
    
    _sql_constraints = [('sql_constraints_name_P', 'unique(name)', 'Ese producto ya existe')]

    def saldo(self):
        listaSocios = self.socio
        listaProducto = self.producto
        for s in listaSocios:            
                for p in listaProducto:    
                    s.saldo = s.saldo + self.kilo*p.precio
                    s.numero_registros=0

    def act_kilos(self):
        listaProducto = self.producto
        
        for p in listaProducto:
            p.kilos=p.kilos+self.kilo

    def calc_año(self):
        self.ensure_one()
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
