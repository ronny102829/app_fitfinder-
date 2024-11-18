import reflex as rx
from ..components.mi_button import mi_button_p
def seccion_pc()->rx.Component:
  return rx.desktop_only(
    rx.heading(
      """¡Transforma tu estilo con un solo clic! Tómate una foto y descubre cómo lucir genial 
      con outfits personalizados solo para ti.""",
      color="#eff9ff",
      size="8",
      width="70%",
      align="center",
      margin_left="7em"

    ),
    rx.heading(
      "con ",
      rx.text.em("fitfinder",color="#92dafe"),
      color="#eff9ff",
      size="9",
      align="center"
    ),
    rx.hstack(
      rx.text(rx.text.em("fitfinder",color="#92dafe",weight="bold"),""" FitFinder propone una solución rápida y personalizada: 
      el usuario toma una foto, y la aplicación le proporciona sugerencias 
      de vestimenta basadas en su aspecto físico, colores, y estilo personal.
       La app puede usar algoritmos de recomendación y filtros de estilos (como casual, formal, deportivo, etc.),
       ayudando a los usuarios a explorar opciones 
       y seleccionar atuendos que se ajusten a sus necesidades y preferencias.""",size="5",color="#42f5cb",width="80vw"),
      rx.box(
        rx.image(src="/moldelo.png",alt="Imagen de app"),
        width="20vw"
      ),
      align="center",
      width="70%",
      margin_left="18em"
    ),
    rx.vstack(
      rx.link(mi_button_p("arrow-down-to-line","descargar app"),href="/login"),
      margin_top="4em",
      align="center"
    ),
  )