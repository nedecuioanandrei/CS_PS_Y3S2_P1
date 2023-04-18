from oldies.core.ui.main_app import OldiesApp, load_context


def main():
    import os
    path = os.path.join(os.getcwd(), "context.json")
    context = load_context(path)
    app = OldiesApp(app_context=context)
    app.mainloop()


if __name__ == "__main__":
    raise SystemExit(main())
