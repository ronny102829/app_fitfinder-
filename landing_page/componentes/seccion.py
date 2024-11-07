import reflex as rx
def seccion()->rx.Component:
  return rx.vstack(
      rx.heading(
        rx.text.span("UpSkill",color=rx.color("blue",7)),
        " la Aplicacion que te enseña"),

      rx.container(
        rx.text("la aplicacion mas divertida que te enseña segun tu progreso con preguntas diarias tendras un",
        rx.text.em(" ranking",color=rx.color("cyan",9)),
        " que te ayudara a medir tus avanzes y podras ",
        rx.text.quote("canjear tus puntos.",color=rx.color("gold",9))),
        rx.link(rx.button(rx.icon(tag="airplay"),"Registrate",margin_top="3em"),href="https://youtube.com"),
      ),
      padding_top="8em",
      align="center",
      text_align="center",
      #background="linear-gradient(0deg, rgba(14,12,135,1) 0%, rgba(0,0,0,1) 100%)",
      height="800px"
    )