# Import gettext module
import gettext

from tm.config import settings

translate = gettext.translation("tablemenu", settings.LOCALE_DIR, fallback=True)
_ = translate.gettext
__ = translate.ngettext
