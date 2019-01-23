# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################
{
  "name"                 :  "Odoo Livechat Tawk To",
  "summary"              :  "Embed live chat in Odoo using Tawk.to",
  "category"             :  "Extra Tools",
  "version"              :  "1.0.0",
  "sequence"             :  45,
  "author"               :  "Webkul Software Pvt. Ltd.",
  "license"              :  "Other proprietary",
  "website"              :  "https://webkul.com/blog/odoo-livechat-tawk/",
  "description"          :  """https://store.webkul.com/Odoo-LiveChat-Tawk-To.html""",
  "live_test_url"        :  "http://odoodemo.webkul.com/?module=odoo_tawk_to&version=11.0",
  "depends"              :  ['website'],
  "data"                 :  [
                             'views/res_config_view.xml',
                             'views/templates.xml',
                            ],
  "demo"                 :['data/demo.xml'],
  "images"               :  ['static/description/Banner.png'],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
  "price"                :  10,
  "currency"             :  "EUR",
  "pre_init_hook"        :  "pre_init_check",
}