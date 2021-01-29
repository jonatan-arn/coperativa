# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime,re
from odoo.exceptions import ValidationError

class producto_model(models.Model):
    _name = 'coperativa.producto_model'
    _description = 'modulo de productos'
    

    name = fields.Char(string="Nombre",index=True,required=True)
    description = fields.Char(string="Descripcion",index=True,required=True)
    precio = fields.Float(String = "precio",index= True,required=True)
    kilos = fields.Float(String = "kilos",index= True,required=True,default=0,readonly=True)
    campana_id_p = fields.One2many("coperativa.campana_model","producto")

    _sql_constraints = [('sql_constraints_name_P', 'unique(name)', 'Ese producto ya existe')]
    


    def borrar_kilos(self):
        listaProducto = self.search(["kilos",">","0"])
        for rec in listaProducto:
            rec.kilos=0

    @api.constrains('precio')
    def validate_precio(self):
        self.ensure_one()
        if not self.comprovar_precio():
            raise ValidationError("Error el precio no puede ser menor de 0")

    def comprovar_precio(self):
        if self.precio<=0:
            return False
        
        return True
