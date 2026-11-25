import flet as ft



def main(page: ft.Page):
    page.title = "Appleの電卓のパクリ"

    result = ft.Text(value="0")

    page.add(result)
if __name__ == "__main__":
    ft.run(main)
