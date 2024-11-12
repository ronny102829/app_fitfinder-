import reflex as rx
from ..components.mi_button import mi_button_p
def seccion_mobile()->rx.Component:
  return rx.mobile_and_tablet(
    rx.heading(
      "Aprende, Juega y Mejora en Programación",
      color="#eff9ff",
      size="8",
      align="center"
    ),
    rx.heading(
      "con ",
      rx.text.em("Up Skill",color="#92dafe"),
      color="#eff9ff",
      size="9",
      align="center"
    ),
    rx.hstack(
      rx.text(rx.text.em("Upskill",color="#92dafe",weight="bold")," es una app diseñada para fortalecer tu aprendizaje en programación a través de quizzes diarios. Responde hasta 5 preguntas al día, sube de nivel y acumula puntos que podrás canjear por recompensas. ¡Únete a la competencia y mejora tus habilidades en programación! Regístrate ahora y empieza a aprender de manera divertida y efectiva.",size="5",color="#eff9ff",text_align="center"),
    ),
    rx.vstack(
      rx.link(mi_button_p("user","Inicia Sesion"),href="/login"),
      margin_top="4em",
      align="center"
    ),
    width="90vw",
  )