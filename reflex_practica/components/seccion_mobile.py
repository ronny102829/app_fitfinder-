import reflex as rx
from ..components.mi_button import mi_button_p
def seccion_mobile()->rx.Component:
  return rx.mobile_and_tablet(
    rx.heading(
      """¡Transforma tu estilo con un solo clic! Tómate una foto y descubre cómo lucir genial 
      con outfits personalizados solo para ti.""",
      color="#eff9ff",
      size="8",
      align="center"
    ),
    rx.heading(
      "con ",
      rx.text.em("fitfinder",color="#92dafe"),
      color="#eff9ff",
      size="9",
      align="center"
    ),
    rx.hstack(
      rx.text(rx.text.em("fitfinder",color="#92dafe",weight="bold"),""" FitFinder propone una solución rápida y 
              personalizada: el usuario toma una foto, y la aplicación le proporciona sugerencias de vestimenta
               basadas en su aspecto físico, colores, y estilo personal. La app puede usar algoritmos de recomendación y filtros de estilos (como casual, formal, deportivo, etc.),
       ayudando a los usuarios a explorar opciones y seleccionar atuendos que se ajusten a sus necesidades y preferencias.""",size="5",color="#eff9ff",text_align="center"),
    ),
    rx.vstack(
      rx.link(mi_button_p("arrow-down-to-line","descargar app"),href="/login"),
      margin_top="4em",
      align="center"
    ),
    width="90vw",
  )