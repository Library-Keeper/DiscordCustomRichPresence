import time
import flet as ft
from json import load, dumps
from pypresence import Presence

from pystray import Icon as icons, Menu as menu, MenuItem as item

from PIL import Image


pid = 1243274739821183006
RPC = Presence(pid)
RPC.connect()
RPC.update(
    state="     ",
    start=int(time.time())
)
config = {}

with open('config.json') as json_file:
    config = load(json_file)

def main(page: ft.Page):
    def open_app(icon, query):
        page.window_skip_task_bar = False
        page.window_to_front()
        page.window_focused = True
        page.update()

    def close_app(icon, query):
        icon.stop()
        page.window_destroy()
        page.update()

    def on_window_change(e):
        if e.data == "minimize":
            e.page.window_skip_task_bar = True
        elif e.data == "close":
            RPC.close()
            tray.stop()
            e.page.window_destroy()
        page.update()

    page.on_window_event = on_window_change

    def nothing(i,q):
        pass

    def open_vk(i,q):
        page.launch_url("https://vk.com/library_keeper")

    def open_tg(i,q):
        page.launch_url("https://t.me/core_library")

    tray = icons(
        name="DiscordCustomRichPresence",
        icon=Image.open("tray_img.png"),
        menu=menu(
            item(
                "Show App",
                open_app
            ),
            item(
                "Close app",
                close_app
            ),
            item(
                "---------",
                nothing,
                enabled=False
            ),
            item(
                "Author:",
                nothing,
                enabled=False
            ),
            item(
                "VK",
                open_vk
            ),
            item(
                "Telegram",
                open_tg
            ),
        )
    )

    def save(e):
        state = "" if page.controls[0].controls[0].controls[1].value == "" else page.controls[0].controls[0].controls[1].value
        details = "" if page.controls[0].controls[1].controls[1].value == "" else page.controls[0].controls[1].controls[1].value
        lit = "" if page.controls[0].controls[2].controls[1].value == "" else page.controls[0].controls[2].controls[1].value
        sit = "" if page.controls[0].controls[3].controls[1].value == "" else page.controls[0].controls[3].controls[1].value
        liu = "" if page.controls[0].controls[4].controls[1].value == "" else page.controls[0].controls[4].controls[1].value
        siu = "" if page.controls[0].controls[5].controls[1].value == "" else page.controls[0].controls[5].controls[1].value
        buttons = "None"
        if page.controls[0].controls[6].controls[1].value:
            b1_text = "" if page.controls[0].controls[6].controls[2].value == "" else page.controls[0].controls[6].controls[2].value
            b1_url = "" if page.controls[0].controls[6].controls[3].value == "" else page.controls[0].controls[6].controls[3].value
            b1 = {"label": b1_text, "url": b1_url}
            buttons = [b1]
            if page.controls[0].controls[7].controls[1].value:
                b2_text = "" if page.controls[0].controls[7].controls[2].value == "" else page.controls[0].controls[7].controls[2].value
                b2_url = "" if page.controls[0].controls[7].controls[3].value == "" else page.controls[0].controls[7].controls[3].value
                b2 = {"label": b2_text, "url": b2_url}
                buttons.append(b2)
        config["state"] = state
        config["details"] = details
        config["lit"] = lit
        config["sit"] = sit
        config["liu"] = liu
        config["siu"] = siu
        config["buttons"] = buttons
        j = dumps(config)
        file = open("config.json", "w")
        file.write(str(j))
        file.close()

    def update(e):
        buttons = None
        state = "     " if page.controls[0].controls[0].controls[1].value == "" else page.controls[0].controls[0].controls[1].value
        details = "     " if page.controls[0].controls[1].controls[1].value == "" else page.controls[0].controls[1].controls[1].value
        lit = "     " if page.controls[0].controls[2].controls[1].value == "" else page.controls[0].controls[2].controls[1].value
        sit = "     " if page.controls[0].controls[3].controls[1].value == "" else page.controls[0].controls[3].controls[1].value
        liu = "     " if page.controls[0].controls[4].controls[1].value == "" else page.controls[0].controls[4].controls[1].value
        siu = "     " if page.controls[0].controls[5].controls[1].value == "" else page.controls[0].controls[5].controls[1].value
        if page.controls[0].controls[6].controls[1].value:
            b1_text = "     " if page.controls[0].controls[6].controls[2].value == "" else page.controls[0].controls[6].controls[2].value
            b1_url = "     " if page.controls[0].controls[6].controls[3].value == "" else page.controls[0].controls[6].controls[3].value
            b1 = {"label": b1_text, "url": b1_url}
            buttons = [b1]
            if page.controls[0].controls[7].controls[1].value:
                b2_text = "     " if page.controls[0].controls[7].controls[2].value == "" else page.controls[0].controls[7].controls[2].value
                b2_url = "     " if page.controls[0].controls[7].controls[3].value == "" else page.controls[0].controls[7].controls[3].value
                b2 = {"label": b2_text, "url": b2_url}
                buttons.append(b2)

        RPC.update(
            state=state,
            details=details,
            large_text=lit,
            small_text=sit,
            large_image=liu,
            small_image=siu,
            buttons=buttons
        )

    def checkbox1(e):
        v = page.controls[0].controls[6].controls[1].value
        vn = page.controls[0].controls[7].controls[1]
        vt1 = page.controls[0].controls[6].controls[2]
        vu1 = page.controls[0].controls[6].controls[3]
        vt2 = page.controls[0].controls[7].controls[2]
        vu2 = page.controls[0].controls[7].controls[3]

        vt1.disabled = not v
        vt1.value = ""
        vu1.disabled = not v
        vu1.value = ""
        vn.disabled = not v
        if not v:
            vn.value = False
            vt2.disabled = True
            vt2.value = ""
            vu2.disabled = True
            vu2.value = ""
        page.update()

    def checkbox2(e):
        v = page.controls[0].controls[7].controls[1].value
        vt = page.controls[0].controls[7].controls[2]
        vu = page.controls[0].controls[7].controls[3]
        vt.disabled = not v
        vt.value = ""
        vu.disabled = not v
        vu.value = ""
        page.update()

    page.title = "DiscordCustomRichPresence"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    width = 500
    height = 740
    page.window_min_height = height
    page.window_min_width = width
    page.window_height = height
    page.window_width = width
    page.window_prevent_close = True
    page.window_maximizable = False
    page.theme = ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.PURPLE, secondary=ft.colors.PINK))
    page.add(
        ft.Column(controls=[
            ft.Row(controls=[
                ft.Text("State: "),
                ft.TextField(str(config["state"]), label="State")
            ]),
            ft.Row(controls=[
                ft.Text("Details: "),
                ft.TextField(str(config["details"]), label="Details")
            ]),
            ft.Row(controls=[
                ft.Text("Large Image Text: "),
                ft.TextField(str(config["lit"]), label="Large Image Text")
            ]),
            ft.Row(controls=[
                ft.Text("Small Image Text: "),
                ft.TextField(str(config["sit"]), label="Small Image Text")
            ]),
            ft.Row(controls=[
                ft.Text("Large Image URL: "),
                ft.TextField(str(config["liu"]), label="Large Image URL")
            ]),
            ft.Row(controls=[
                ft.Text("Small Image URL: "),
                ft.TextField(str(config["siu"]), label="Small Image URL")
            ]),
            ft.Row(controls=[
                ft.Text("B 1: "),
                ft.Checkbox(on_change=checkbox1, value=True if config["buttons"] != "None" else False),
                ft.TextField(
                    label="Text",
                    width=page.width/7,
                    disabled=False if config["buttons"] != "None" else True,
                    value=str(config["buttons"][0]["label"]) if config["buttons"] != "None" else ""
                ),
                ft.TextField(
                    label="URL",
                    width=page.width/7,
                    disabled=False if config["buttons"] != "None" else True,
                    value=str(config["buttons"][0]["url"]) if config["buttons"] != "None" else ""
                )
            ]),
            ft.Row(controls=[
                ft.Text("B 2: "),
                ft.Checkbox(
                    on_change=checkbox2,
                    disabled=True if config["buttons"] == "None" else False,
                    value=True if len(config["buttons"]) > 1 and config["buttons"] != "None" else False
                ),
                ft.TextField(
                    label="Text",
                    width=page.width / 7,
                    disabled=False if len(config["buttons"]) > 1 and config["buttons"] != "None" else True,
                    value=str(config["buttons"][1]["label"]) if len(config["buttons"]) > 1 and config["buttons"] != "None" else ""
                ),
                ft.TextField(
                    label="URL",
                    width=page.width / 7,
                    disabled=False if len(config["buttons"]) > 1 and config["buttons"] != "None" else True,
                    value=str(config["buttons"][1]["url"]) if len(config["buttons"]) > 1 and config["buttons"] != "None" else ""
                )
            ]),
            ft.Row(controls=[
                ft.Text("Update: "),
                ft.TextButton("Update", on_click=update),
                ft.TextButton("Sаve as Default", on_click=save)
            ]),
            ft.Row(controls=[
                ft.Text("Author"),
                ft.TextButton("VK", url="https://vk.com/library_keeper"),
                ft.TextButton("Telegram", url="https://t.me/core_library"),
            ]),
        ])
    )
    page.update()

    tray.run()
ft.app(main)