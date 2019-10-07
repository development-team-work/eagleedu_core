# -*- coding: utf-8 -*-

{
    'name': "Eagle Education Core",
    'version': '1.1',
    'summary': """This is a e education manament system""",
    'description': """
This module for This is a e education manament system 
    """,
    'author': "Eagle ERP",
    'website': "http://www.eagle-erp.com",
    'support': 'info@eagle-erp.com',
    'category': 'Education',
    'depends': [
                'base',
                ],
    'data':[
            'views/eagleedu_application.xml',
            'views/eagleedu_student.xml',
            'security/ir.model.access.csv',
            'reports/print_reports.xml',
            'reports/report_eagleedu_registration.xml',
    ],
    'installable' : True,
    'application' : False,
}

