import PageTemplate.MainWindow_support as guiSupport
import PageTemplate.MainWindow as gui
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)


gui.vp_start_gui()
