import reflex as rx
from .componentes.navbar import navbar
from .componentes.seccion import seccion
from .componentes.cambiar_tema import cambiar_tema

# si deseamos tener border en nuestros componentes en relacion a nuestra ventana rx.container
# si deseamos que nuestros componetes ocupen el 100% en relacion a nuestra ventana rx.box
# si deseamos que nuestros componentes se han flexibles en relacion a nuestra ventana dependiendo su distribucion rx.vstack o rx.hstack (rx.flex)
def index()->rx.Component:
  return rx.box(
    navbar(),
    cambiar_tema(),
    seccion(),
  )

app=rx.App(
  theme=rx.theme(
    appearance="light",
    has_background=True,
    radius="large",
    accent_color="teal",
  )
)
app.add_page(index)