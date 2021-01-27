# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime,re
from odoo.exceptions import ValidationError

class socio_model(models.Model):
    _name = 'coperativa.socio_model'
    _description = 'modulo de socios'
    
    id_socio = fields.Integer(String = "id del socio",index= True,required=True)
    foto = fields.Binary(String = "Foto",index= True,required=False)
    name = fields.Char(string="Nombre",index=True,required=True)
    apellidos = fields.Char(string="Apellidos",index=True,required=True)
    dni = fields.Char(string="Dni",index=True,required=True)
    fechaAlta = fields.Date(string="Fecha de alta del socio",index=True,required=True,default=fields.date.today())
    telf = fields.Integer(String = "telefono",index= True,required=True,size="9")
    email = fields.Char(string="correo electronico",index=True,required=True)
    saldo = fields.Float(string="Saldo del socio",default=0,readonly=True)
    campana_id_s = fields.One2many("coperativa.campana_model","socio")
    numero_registros = fields.Integer(string="numero de registros",default=0,compute="setRegistro")
    _sql_constraints = [('sql_constraints_dni', 'unique(dni)', 'Ese dni ya existe'),
    ('sql_constraints_id', 'unique(id_socio)', 'Ese id socio ya existe')]
    
    def setRegistro(self):
        self.numero_registros=len(self.campana_id_s)
        
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