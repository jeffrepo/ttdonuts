# -*- coding: utf-8 -*-


{
    'name': 'Taste top donuts',
    'version': '1.1',
    'category': 'Sales/Point of Sale',
    'sequence': 100,
    'summary': 'Módulo para Taste top donuts',
    'description': """
        Taste top donuts
    """,
    'depends': ['base','point_of_sale'],
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
