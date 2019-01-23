#
#    Copyright (c) 2017-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#
##########################################################################

from odoo import http
from odoo.http import request
from odoo import SUPERUSER_ID
from odoo.addons.web.controllers.main import WebClient, Binary, Home
import werkzeug.utils
import logging
import odoo
import json
_logger = logging.getLogger(__name__)

class Home(Home):


    @http.route('/wk/tawk/to/', type='json', auth='public')
    def wk_tawk_to(self, **kw):
        ir_default = request.env['ir.default'].sudo()
        tawk_site_id = ir_default.get(
            'res.config.settings', 'tawk_site_id')
        visible_on = ir_default.get(
            'res.config.settings', 'visible_on')
        if tawk_site_id:
            request.session['wk_tawk_to_site_id'] = tawk_site_id
            request.session['wk_tawk_visible_on'] = visible_on
            _logger.info('----------------------------%r',request.session)
            return True
        return False
       



