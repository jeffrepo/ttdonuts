# -*- coding: utf-8 -*-
{
    'name': 'Taste top donuts',
    'version': '1.1',
    'category': 'Sales/Point of Sale',
    'sequence': 100,
    'author': "Jefferson Sila",
    'summary': 'Módulo para Taste top donuts, reportes',
    'description': """
        Taste top donuts
    """,
    'depends': ['base','point_of_sale','stock','account'],
    'license': 'LGPL-3',
    'data': [
        'views/stock_picking_views.xml',
        'report/report_picking.xml',
    ],
    # 'assets':{
    #     'point_of_sale.assets': [
    #         'ttdonuts/static/src/js/**/*.js',
    #     ],
    #     'web.assets_qweb':[
    #         'ttdonuts/static/src/xml/**/*.xml',
    #     ],
    #     'web.assets_backend': [
    #     ],
    # },
}
