from taipy.gui import Gui

index = """
<p>Hello World!!</p>
>
"""

app = Gui(page=index)

if __name__ == "__main__":
    app.run(use_reloader=True)