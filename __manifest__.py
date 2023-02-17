# -*- coding: utf-8 -*-


{
    'name': 'Taste top donuts',
    'version': '1.0',
    'category': 'Hidden',
    'sequence': 6,
    'summary': 'Módulo para Taste top donuts',
    'description': """

""",
    'depends': ['base','point_of_sale'],
    'data': [

    ],
    'assets':{
        'point_of_sale.assets': [
            'ttdonuts/static/src/js/**/*.js',
        ],
        'web.assets_qweb':[
            'ttdonuts/static/src/xml/**/*.xml',
        ],
        'web.assets_backend': [
        ],
    },
    'installable': True,
    'auto_install': False,
}
