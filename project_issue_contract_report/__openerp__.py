# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 Vincent Renaville
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

{
    'name': 'Project Issue relate contract hours',
    'summary': 'Print Ticket linked to a contract',
    'version': '1.1',
    'category': 'Project Management',
    'description': """
    Report on Project Issue linked to a project
    set in invoice line of the related block hours
""",
    'author': "Vincent Renaville,Odoo Community Association (OCA)",
    'depends': [
        'project_issue',
        'account',
        'project_stage_state',
        ],
    'data': [
        'report.xml',
        'views/report_contract_issue.xml',
        'views/report_history_issue.xml'
        ],
    'installable': True,
}
