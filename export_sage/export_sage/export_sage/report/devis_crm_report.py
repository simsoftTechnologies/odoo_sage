# -*- coding: utf-8 -*-
import logging
import time
from odoo import api, models
from datetime import datetime
import calendar
from calendar import monthrange
from datetime import date
from operator import itemgetter, attrgetter ,methodcaller
_logger = logging.getLogger(__name__)

class report_devis_sous_contrat(models.AbstractModel):
  _name = 'report.crm_simsoft.sous_contrate'

  @api.multi
  def render_html(self,  ids ,data):
  
    docargs = {
      'doc_ids': self.ids,
      # 'doc_model': self.model,
      # 'data': data['form'],
      'time': time,
      
    }
    return self.env['report'].render('crm_simsoft.sous_contrate', docargs)
