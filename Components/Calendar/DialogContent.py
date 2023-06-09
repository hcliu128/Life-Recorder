from datetime import date

from libs.kivymd_package import *
from Components.Calendar.EventCard import color_list

class DialogContent(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__add_title_input_layout()
        self.__add_date_input_layout()
        self.__add_button_layout()

    def show_date_picker(self, _):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_save)
        date_dialog.open()

    def on_date_save(self, instance, value, date_range):
        self.selected_date = value
        self.date_text.text = value.strftime('%Y/%m/%d')

    def color_button_on_press(self, _):
        self.__menu.open()

    def __add_date_input_layout(self):
        date_input_layout = MDGridLayout(rows=1)

        self.date_text = MDTextField(
            text=date.today().strftime('%Y/%m/%d'),
            validator="date",
            date_format="yyyy/mm/dd",
            required=True
        )
        date_picker = MDIconButton(
            icon='calendar',
            on_release=self.show_date_picker,
            padding='20dp'
        )
        self.color_index = 0
        self.__color_button = MDIconButton(
            icon="circle",
            theme_icon_color="Custom",
            text_color=color_list[self.color_index]
        )
        self.__color_button.bind(on_release=self.color_button_on_press)
        menu_items = self.__get_color_menu(color_list[self.color_index])

        self.__menu = MDDropdownMenu(
            caller=self.__color_button,
            items=menu_items,
            position="center",
            width_mult=1,
            elevation=2
        )
            
        date_input_layout.add_widget(self.date_text)
        date_input_layout.add_widget(date_picker)
        date_input_layout.add_widget(self.__color_button)
        self.add_widget(date_input_layout)

    def __add_title_input_layout(self):
        
        self.event_title = MDTextField(
            hint_text="Title",
            max_text_length=30,
            required=True
        )

        self.add_widget(self.event_title)

    def __add_button_layout(self):
        button_layout = MDBoxLayout(orientation="horizontal")

        self.save_button = MDRaisedButton(text="SAVE")
        self.cancel_button = MDFlatButton(text="CANCEL")

        button_layout.add_widget(self.save_button)
        button_layout.add_widget(self.cancel_button)
        self.add_widget(button_layout)

    def __get_color_menu(self, color_active):
        menu_items = []
        for color in color_list:
            menu_item = {
                "id": color,
                "viewclass": "MDIconButton",
                "icon": "circle",
                "theme_icon_color": "Custom",
                "text_color": color,
                "on_release": lambda x=color: self.__color_on_press(x)
            }
            if color_active == color:
                menu_item["icon"] = "check-circle"
            menu_items.append(menu_item)
        return menu_items

    def __color_on_press(self, color):
        menu_items = self.__get_color_menu(color)
        self.__color_button.text_color = color
        self.__menu.dismiss()
        self.color_index = color_list.index(color)
        self.__menu = MDDropdownMenu(
            caller=self.__color_button,
            items=menu_items,
            position="center",
            width_mult=1,
            elevation=2
        )
        