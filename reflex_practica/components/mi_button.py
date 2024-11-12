import reflex as rx
#button primario
def mi_button_p(icon,text)->rx.components:
  return rx.button(
    rx.icon(icon,size=25),
    text,
    size="3",
    variant="solid",
    radius="full",
    background="#173154",
    color="#eff9ff",
    border="solid #eff9ff"
  )
#button secundario
def mi_button_s(icon,text)->rx.Component:
  return rx.button(
    rx.icon(icon,size=25),
    text,
    size="3",
    variant="surface",
    radius="full",
    background="#eff9ff"
  )