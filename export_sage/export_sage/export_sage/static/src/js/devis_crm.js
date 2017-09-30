odoo.define('crm_simsoft.devis_crm', function (require) {

var core = require('web.core');
var data = require('web.data');
var ActionManager = require('web.ActionManager');
var form_common = require('web.form_common');
var time = require('web.time');
var _t = core._t;
var QWeb = core.qweb;
var Model = require('web.DataModel');
    
var RoomSummary = form_common.FormWidget.extend(form_common.ReinitializeWidgetMixin, {
        display_name: _t('Form'),
        view_type: "form",
        init: function() {
            this._super.apply(this, arguments);
            if(this.field_manager.model == "sale.order")
            {
                $(".oe_view_manager_buttons").hide();
                $(".oe_view_manager_header").hide();
                
                    $( ".o_sub_menu").animate({
                          width: 'toggle'
                      });
                          $( ".o_sub_menu").find('img').animate({
                          width: 'toggle'
                      });

                  
               }
            
            
            
          
            
           
            
           
           
//            
        },
             
    });
});
