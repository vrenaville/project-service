# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Vincent Renaville
#    Copyright 2015 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, api
from lxml import html
from lxml.html.clean import Cleaner


class ProjectIssue(models.Model):
    _inherit='project.issue'

    @api.multi
    def get_issue_message(self):
        message = []
        mail_message_obj = self.env['mail.message']
        message_rst = mail_message_obj.search([('res_id', 'in',
                                            self.ids),
                                            ('model', '=', 'project.issue'),
                                            ('subtype_id', '<>', False),
                                            ('type','=','comment')],
                                            order='date desc')
        doc_cleaner = Cleaner(style=True, links=True,
                          add_nofollow=True,
                          page_structure=False,
                          safe_attrs_only=False)
        for mes in message_rst:
            doc_raw = html.document_fromstring(mes.body)
            doc = doc_cleaner.clean_html(doc_raw)
            value_body = html.tostring(doc)
            messi = {'date': mes.date,
                     'subject': mes.subject,
                     'body': value_body
                     }
            message.append(messi)
        print str(message)
        return message
