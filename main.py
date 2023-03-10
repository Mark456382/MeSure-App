import sys
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
# > Typing
from typing import Dict, Any
# > Rich
from rich.console import Console

# > Init
console = Console()
DEBUG = True

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
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        
        root: MDScreen = Builder.load_file("main.kv")
        
        if DEBUG:
            console.print(root.ids) # Если у объекта в файле main.kv прописан id, то они будут в root.ids

        return root
    
    def on_start(self):
        if DEBUG:
            self.fps_monitor_start()

# > Start
app = MeSureMVPApp()
app.run()