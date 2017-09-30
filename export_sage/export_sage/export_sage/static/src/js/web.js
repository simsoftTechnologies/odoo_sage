odoo.define('crm_simsoft.web_clock', function(require) {
"use strict";
    var Model = require('web.DataModel');
    var SystrayMenu = require('web.SystrayMenu');
    var Widget = require('web.Widget');
    var Users = new Model('res.users');

     var WebClock = Widget.extend({
        template: 'WebClock',
        renderElement:function(){
            var self = this;
            self._super();
            $(".dashboard-wrapper").before("<span class='add_clock'></span>")
            $(".o_cp_right").after("<span class='add_clock'></span>")
         
            var width =$( window ).width();
            if(width >50){
                $(".add_clock").show();
            }
            else{
                $(".add_clock").hide();

            }
          /*  $(window).resize(function(){
                var width =$( window ).width();
                if(width <100){
                    $(".add_clock").show();
                }
                else{
                    $(".add_clock").hide();

                }
            });*/
           function startTime() {
                var today = new Date();
                var h = today.getHours();
                var m = today.getMinutes();
                var s = today.getSeconds();
                m = checkTime(m);
                s = checkTime(s);
                $('#web_clock').html(h + ":" + m + ":" + s);
                var t = setTimeout(startTime, 500);
            }
            function checkTime(i) {
                if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
                return i;
            }

            function formatAMPM() {
                var date = new Date();
                var currDate = date.getDate();
                var hours = date.getHours();
                var dayName = getDayName(date.getDay());
                var minutes = date.getMinutes();
                var monthName = getMonthName(date.getMonth());
                var year = date.getFullYear();
                var ampm = hours >= 12 ? 'PM' : 'AM';
                var s = date.getSeconds();
                hours = hours % 12;
                hours = hours ? hours : 12; // the hour '0' should be '12'
                minutes = minutes < 10 ? '0' + minutes : minutes;
                s = checkTime(s);
                var strTime = currDate + ' ' + monthName + ' ' + hours + ':' + minutes + ':' + s +' '+ ampm;
                $('#web_clock').html(strTime);
                $(".add_clock").html('<i style="font-size: 21px;color: white;">'+strTime+'</i>');
                var t = setTimeout(formatAMPM, 500);
            }

            function getMonthName(month) {
                var ar = new Array("Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sep", "Octr", "Nov", "Dec");
                return ar[month];
            }

            function getDayName(day) {
                var ar1 = new Array("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat");
                return ar1[day];
            }
            formatAMPM()
        },
    });

     Users.call('has_group', ['base.group_system']).done(function(is_employee) {
        if (is_employee) {
             SystrayMenu.Items.push(WebClock);
        }
    });

});