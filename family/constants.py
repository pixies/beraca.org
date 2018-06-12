from django.utils.translation import ugettext_lazy as _

SEX_CHOICES = ((_('Masculino'),_('Masculino')),
               (_('Feminino'),_('Feminino')))


LAND_SITUATION_CHOICES = (
    (_("Posse"), _("Posse")),
    (_("Arrendamento"), _("Arrendamento")),
    (_("Titulado"), _("Titulado")),
    (_("Territorio Indígena"), _("Territorio Indígena")),
    (_("Unidade de Conservação"), _("Unidade de Conservação")),
    (_("Território Quilombola"), _("Território Quilombola"))
)

HAS_CAR_CHOICES = (
    (_("Sim"), _("Sim")),
    (_("Não"), _("Não")),
)

GEOREFERENCING_CHOICES = (
    (_("Geodésico"), _("Geodésico")),
    (_("Navegação"), _("Navegação")),
    (_("Outro"), _("Outro")),
)

AGE_GROUP_CHOICES = (
    (_("Crianças (0 a 5 anos)"), _("Crianças (0 a 5 anos)")),
    (_("Crianças (6 a 11 anos)"), _("Crianças (6 a 11 anos)")),
    (_("Crianças (12 a 17 anos)"), _("Crianças (12 a 17 anos)")),
)

SCHOLL_BUS_CHOICES = (
    (_("Não vai a escola"), _("Não vai a escola")),
    (_("A pé"), _("A pé")),
    (_("Bicicleta"), _("Bicicleta")),
    (_("Carona"), _("Carona")),
    (_("Barco"), _("Barco")),
    (_("Canoa"), _("Canoa")),
    (_("Ônibus"), _("Ônibus")),
)

NEGOTIATION_PRECESS_CHOICES = (
    (_("Sim"), _("Sim")),
    (_("Não"), _("Não")),
)

UNDERSTAND_PROCESS_BUY_RAW_MATERIAL_CHOICES = (
    (_("Sim"), _("Sim")),
    (_("Não"), _("Não")),
)

HAS_PURCHASE_RECEIPT_CHOICES = (
    (_("Sim, sempre"), _("Sim, sempre")),
    (_("Sim, às vezes"), _("Sim, às vezes")),
    (_("Não"), _("Não")),
)

UNDERSTAND_PURCHASE_RECEIPT_NOTES_CHOICES = (
    (_("Sim"), _("Sim")),
    (_("Não"), _("Não")),
)

RECEIPT_FILING_CHOICES = (
    (_("Sim, sempre"), _("Sim, sempre")),
    (_("Sim, às vezes"), _("Sim, às vezes")),
    (_("Não"), _("Não")),
)

SCANNING_FILES_CHOICES = (
    (_("Sim"), _("Sim")),
    (_("Não"), _("Não")),
)

DIFFICULTIES_TO_COMMERCIALIZE_CHOICES = (
    (_("Sim"), _("Sim")),
    (_("Não"), _("Não")),
)

SATISFACTION_WITH_STAGES_WORK_CHOICES = (
    (_("Muito satisfeito"), _("Muito satisfeito")),
    (_("Satisfeito"), _("Satisfeito")),
    (_("Precisa melhorar"), _("Precisa melhorar")),
    (_("Pouco satisfeito"), _("Pouco satisfeito")),
    (_("Nada satisfeito"), _("Nada satisfeito")),
)

ORGANIC_CERTIFICATES_CHOICES = (
    (_("Sim"), _("Sim")),
    (_("Não"), _("Não")),
)

USE_EPI_CHOICES = (
    (_("Completo"), _("Completo")),
    (_("Parcialmente"), _("Parcialmente")),
    (_("Não utiliza"), _("Não utiliza")),
)

HOW_GET_EPI_CHOICES = (
    (_("Comprados com recurso próprio"), _("Comprados com recurso próprio")),
    (_("Ganhou da empresa"), _("Ganhou da empresa")),
    (_("Ganhou de parceiros"), _("Ganhou de parceiros")),
    (_("Emprestado"), _("Emprestado")),
)

