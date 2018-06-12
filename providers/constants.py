from django.utils.translation import ugettext_lazy as _

EPI_CHOICES = ((_('completo'),_('Completo')),
               (_('parcialmente'),_('Parcialmente')),
               (_('nao_utiliza'),_('Não utiliza')))

EPI_ORIGIN_CHOICES = ((_('comprados_com_recurso_proprio'),_('Comprados com recurso próprio')),
                      (_('ganhou_da_empresa'),_('Ganhou da empresa')),
                      (_('ganhou_de_parceiros'),_('Ganhou de parceiros')),
                      (_('emprestado'),_('Emprestado')))

HYGIENE_CHOICES = ((_('nao_controla'),_('Não controla')),
                           (_('controla_parcialmente'),_('Controla parcialmente')),
                           (_('controla_totalmente_o_local'),_('Controla totalmente o local')))

DRY_ROOF_TYPE_CHOICES = ((_('area_propria'),_('Área própria')),
                         (_('area_compartilhada'),_('Área compartilhada')),
                         (_('area_cedida'),_('Área cedida')),
                         (_('organizacao'),_('Organização')))