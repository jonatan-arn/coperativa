# -*- coding: utf-8 -*-

from odoo import models, fields, api
import re
from datetime import datetime
from odoo.exceptions import ValidationError

class socio_model(models.Model):
    _name = 'coperativa.socio_model'
    _description = 'modulo de socios'
    
    id_socio = fields.Integer(String = "id del socio",index= True,required=True)
    foto = fields.Binary(String = "Foto",required=False)
    name = fields.Char(string="Nombre",required=True)
    apellidos = fields.Char(string="Apellidos",required=True)
    dni = fields.Char(string="Dni",index=True,required=True)
    fechaAlta = fields.Date(string="Fecha de alta del socio",required=True,default=lambda self:datetime.today())
    telf = fields.Char(String = "telefono" ,required=True)
    email = fields.Char(string="correo electronico",required=True)
    saldo = fields.Float(string="Saldo del socio",default=0,readonly=True)
    registros = fields.One2many("coperativa.campana_model","socio",string="Registros de las campañas")
    numero_registros = fields.Integer(string="numero de registros",default=0,compute="setRegistro")
    _sql_constraints = [('sql_constraints_dni', 'unique(dni)', 'Ese dni ya existe'),
    ('sql_constraints_id', 'unique(id_socio)', 'Ese id socio ya existe')]
    


    @api.constrains('telf')
    def validate_telf(self):
        if len(self.telf)!=9:
            raise ValidationError("Error telefono menor de 9 digitos")


    def setRegistro(self):
        self.numero_registros=len(self.registros)
        
    @api.constrains('email')
    def validate_email(self):
        if not self.comprovar_email(self.email):
            raise ValidationError("Error al introducir en el email")

    
    
    @api.constrains('dni')
    def validate_dni(self):
        if not self.comprovar_dni(self.dni):
            raise ValidationError("Error al introducir el dni")
        


    def comprovar_email(self,email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            return True
        
        return False
    def comprovar_dni(self,nif):
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        numeros = "1234567890"
        if (len(nif) == 9):
            letraControl = nif[8].upper()
            dni = nif[:8]
            if ( len(dni) == len( [n for n in dni if n in numeros] ) ):
                if tabla[int(dni)%23] == letraControl:
                    return True
        return False               