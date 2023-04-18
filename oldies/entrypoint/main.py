import sys
from oldies.core.ui.main_app import OldiesApp, load_context


def main(argv=None):
    context = load_context()
    app = OldiesApp(app_context=context)
    app.mainloop()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
