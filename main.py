from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
# > Typing
from typing import Dict, Any
# > Rich
from rich.console import Console
# > Local Import
from settings import DEBUG, THEME_STYLE, PRIMARY_PALETTE, MAIN_UI_FILE

# > Init
console = Console()

# > Functions
def lsattr(obj: object) -> Dict[str, Any]:
    """Return attributes of object."""
    d = {}
    for i in dir(obj):
        d[i] = getattr(obj, i)
    return d

# > Main
class MeSureMVPApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = THEME_STYLE
        self.theme_cls.primary_palette = PRIMARY_PALETTE
        
        root: MDScreen = Builder.load_file(MAIN_UI_FILE)

        if DEBUG: 
            console.print(root.ids) # Если у объекта в файле main.kv прописан id, то они будут в root.ids

        return root
    
    def on_start(self):
        if DEBUG:
            self.fps_monitor_start()

# > Start
if __name__ == "__main__":
    app = MeSureMVPApp()
    app.run()
