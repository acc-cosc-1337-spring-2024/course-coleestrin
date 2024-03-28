def add_inventory(widgets: dict, widget_name: str, quantity: int):
    widgetVal = widgets.get(widget_name)
    
    if (widgetVal):
        widgets.update({widget_name: widgetVal + quantity})
    else:
        widgets.update({widget_name: quantity})

def remove_inventory_widget(widget_name: str, widgets: dict):
    if (widgets.get(widget_name)):
        widgets.pop(widget_name)
        return "Record deleted"
    else:
        return "Item not found"