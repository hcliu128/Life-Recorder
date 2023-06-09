from libs.kivymd_package import *

class TaskItem(ThreeLineAvatarIconListItem):
    def __init__(self, pk=None, priority=1, **kwargs):
        super().__init__(**kwargs)
        self.delete_button = MDIconButton(
            icon='trash-can-outline',
            theme_text_color="Custom",
            text_color=[1, 0, 0, 1]
        )
        self.category = MDIconButton(
            icon='star',
            theme_text_color="Custom",
            text_color=[255/256, 192/256, 0/256, 1],
            pos_hint={"center_x": .5, "center_y": .5}
        )
        self.priority = MDLabel(text=f"{priority}")
        self.pk = pk
        self._add_check()
        self._add_right_items()

    def _add_check(self):
        self.check = LeftCheckbox()
        self.add_widget(self.check)

    def _add_right_items(self):
        self.right_items = RightItems()
        
        self.right_items.add_widget(self.category)
        self.right_items.add_widget(self.priority)
        self.right_items.add_widget(self.delete_button)
        self.ids._right_container.width = self.right_items.width
        self.ids._right_container.x = self.right_items.width
        self.add_widget(self.right_items)



class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    '''Custom left container'''

class RightItems(IRightBodyTouch, MDBoxLayout):
    adaptive_width = True
