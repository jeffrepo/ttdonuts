odoo.define('ttdonuts.ProductScreen', function(require) {
    'use strict';

    const { useState, useExternalListener } = owl.hooks;
    const { useListener } = require('web.custom_hooks');
    const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');
    const ProductScreen = require('point_of_sale.ProductScreen')

    const TtdonutsProductScreen = ProductScreen =>
        class extends ProductScreen {
            constructor(){
                super(...arguments);
            }
            _onClickPay() {
                const linea_cero = this.currentOrder
                    .get_orderlines()
                    .filter(line => line.get_quantity() <= 0 || line.price <= 0)
                    .find(line => line.get_quantity() * line.price === 0);
                if (linea_cero){
                    this.showPopup('ErrorPopup', {
                        title: this.env._t('Producto a cero'),
                        body: this.env._t('No puede vender producto a $0.00'),
                    });
                    return;
                }else{
                    super._onClickPay();
                }

            }
        };

    Registries.Component.extend(ProductScreen, TtdonutsProductScreen);

    return TtdonutsProductScreen;
});
