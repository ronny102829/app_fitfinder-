import reflex as rx
from ..components.seccion_pc import seccion_pc
from ..components.seccion_mobile import seccion_mobile
def seccion()->rx.Component:
  return rx.section(
    seccion_pc(),
    seccion_mobile(),
  )