import reflex as rx
from reflex.style import set_color_mode,color_mode,toggle_color_mode

def cambiar_tema()->rx.Component:
  return rx.hstack(
    rx.button(rx.icon(tag="sun", size=20),on_click=toggle_color_mode,variant="outline"),
    justify="end",
  )
