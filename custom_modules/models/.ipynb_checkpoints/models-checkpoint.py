# Importar la librería de Odoo
import odoo

# Iniciar sesión en Odoo
odoo.api.Environment.manage().login()

# Buscar el diario de ventas que utilizas para las facturas rectificativas
journal = odoo.env['account.journal'].search([('type', '=', 'sale_refund')])

# Cambiar la cuenta de ingreso utilizada en el diario de ventas
journal.default_credit_account_id = ID_DE_LA_CUENTA_4175

# Guardar los cambios en el diario de ventas
journal.save()

# Cerrar la sesión de Odoo
odoo.api.Environment.manage().logout()