import reflex as rx
from ..components.mi_button import mi_button_s
def navbar()->rx.Component:
  return rx.box(
    rx.desktop_only(
      rx.hstack(
        rx.heading("UpSkill",color="#eff9ff"),
        rx.hstack(
          rx.link(
            rx.icon("youtube",color="#eff9ff")
          ),
          rx.link(
            rx.icon("github",color="#eff9ff")
          ),
          rx.link(
            mi_button_s("user","Iniciar Sesion"),
            href="/login"
          ),
          justify="end",
          spacing="5",
          align_items="center"
        ),
        justify="between",
        align_items="center"
      ),
    ),
    rx.mobile_and_tablet(
      rx.hstack(
        rx.heading("UpSkill",color="#eff9ff"),
        rx.hstack(
          rx.link(
            mi_button_s("user","Iniciar Sesion"),
            href="/login"
          ),
          justify="end"
        ),
        justify="between",
        align_items="center"
      )
    ),
    bg="#1d4f8b",
    #rx.color("#E9F1FA", 3),
    padding="1em",
    # position="fixed",
    # top="0px",
    # z_index="5",
    width="100%",
  )