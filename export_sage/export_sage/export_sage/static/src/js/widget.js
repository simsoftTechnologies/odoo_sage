odoo.define('hotel_management_simsoft.widget', function (require) {
    var core = require('web.core');
    var FormView = require('web.FormView');
    var FieldChar = core.form_widget_registry.get('char');
    var _super_getDir = jscolor.getDir.prototype;
    jscolor.getDir = function () {
        var dir = _super_getDir.constructor();
        if (dir.indexOf('hotel_management_simsoft') === -1) {
            jscolor.dir = 'hotel_management_simsoft/static/lib/jscolor/';
        }
        return jscolor.dir;
    };


    var FieldColor = FieldChar.extend({
        template: 'FieldColor',
        start: function () {
            this._super.apply(this, arguments);
        },
        is_syntax_valid: function () {
            var $input = this.$('input');
            if (!this.get("effective_readonly") && $input.size() > 0 && $input.val()) {
                var val = $input.val();
                var isOk = /^#[0-9A-F]{6}$/i.test(val);
                if (!isOk) {
                    return false;
                }
                try {
                    this.parse_value(this.$('input').val(), '');
                    return true;
                } catch (e) {
                    return false;
                }
            }
            return true;
        },
        render_value: function () {
            var show_value = this.format_value(this.get('value'), '');
            if (!this.get("effective_readonly")) {
                var $input = this.$el.find('input');
                $input.val(show_value);
                $input.css("background-color", show_value);
                jscolor.init(this.$el[0]);
            } else {
                this.$(".oe_form_char_content").text(show_value);
                this.$('div').css("background-color", show_value)
            }
        }
    });
    core.form_widget_registry.add('color', FieldColor);
    FormView.include({
        to_edit_mode: function () {
            this._super();
            jscolor.init(this.$el[0]);
        }
    });

});
