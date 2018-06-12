from django.utils.translation import ugettext_lazy as _
from django.utils.dates import MONTHS


PROVENANCE_TYPE = (
    (_("Natural"), _("Natural")),
    (_("Plantio"), _("Plantio")),
    (_("SAF"), _("SAF")),
)

COLLECTION_TYPE = (
    (_("Área própria"), _("Área própria")),
    (_("Área compartilhada"), _("Área compartilhada")),
    (_("Área cedida"), _("Área cedida")),
    (_("Praia"), _("Praia")),
    (_("Rio"), _("Rio")),
)

BS_CHOICES = (
    (_("Patrimônio genético"), _("Patrimônio genético")),
    (_("CTA identificável"), _("CTA identificável")),
    (_("CTA não identificável"), _("CTA não identificável")),
)

MONTHS_CHOICES = [(MONTHS[i], MONTHS[i]) for i in MONTHS]