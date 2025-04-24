import flet

class MediaQueryManager:
    def __init__(self,page:flet.Page):
        self.breakpoints = {
        }
        self.listeners = {
        }
        self.current_break_point = None
    def on_resized(self,event:flet.WindowResizeEvent):
        width = event.width
        for name,(min_width,max_width) in self.breakpoints.items():
            if max_width >= width > min_width:
                if self.current_break_point != name:
                    self.current_break_point = name
                    for func in self.listeners[name]:
                        func()

class MediaQuery:
    def __init__(self,page:flet.Page):
        if not hasattr(page, '_media_query'):
            page._media_query = MediaQueryManager(page)
        self.page = page

    def handler(event):
        event.page._media_query.on_resized(event)
    def on(self,point,callback_function):
        self.page._media_query.listeners[point].append(callback_function)
    def off(self,point,callback_function):
        self.page._media_query.listeners[point].remove(callback_function)
        
    def register(self,point,min_width,max_width):
        self.page._media_query.breakpoints[point] = (min_width,max_width)
        self.page._media_query.listeners[point] = []
        