import pygame
from pygame_gui.elements.ui_button import UIButton
from pygame_gui.core import ObjectID
from pygame_gui.core.interfaces import IContainerLikeInterface, IUIManagerInterface
from pygame_gui.core.ui_element import UIElement
from typing import Union, Tuple, Dict


class Toggle(UIButton, UIElement):
    def __init__(self, relative_rect: pygame.Rect, text: (str, str), manager: IUIManagerInterface,
                 font: pygame.font.Font):
        self.first_text, self.second_text = text
        UIButton.__init__(self, relative_rect=relative_rect, text=self.first_text, manager=manager)
        self.showed_text = self.first_text
        self._click_count = 0

    def update(self, time_delta: float):
        UIElement.update(self, time_delta)
        if self.alive():
            # 0,1 -> +(text.first) ; 2,3 -> -(text.second)
            # clear pressed state, we only want it to last one update cycle
            self.pressed = False

            if self.pressed_event:
                # if a pressed event has occurred set the button to the pressed state for one cycle.
                self.pressed_event = False
                self.pressed = True
                self._click_count += 1
                print(self._click_count)

            if self._click_count % 2 < 1:
                self.set_text(self.first_text)
            else:
                self.set_text(self.second_text)

        # print(self.font.size("+"))

    def _create_valid_ids(self,
                          container: Union[IContainerLikeInterface, None],
                          parent_element: Union[None, 'UIElement'],
                          object_id: Union[ObjectID, str, None],
                          element_id: str):
        """
        Creates valid id lists for an element. It will assert if users supply object IDs that
        won't work such as those containing full stops. These ID lists are used by the theming
        system to identify what theming parameters to apply to which element.

        :param container: The container for this element. If parent is None the container will be
                          used as the parent.
        :param parent_element: Element that this element 'belongs to' in theming. Elements inherit
                               colours from parents.
        :param object_id: An optional set of IDs to help distinguish this element
                         from other elements.
        :param element_id: A string ID representing this element's class.

        """
        if parent_element is None and container is not None:
            id_parent = container
        else:
            id_parent = parent_element

        if isinstance(object_id, str):
            if object_id is not None and ('.' in object_id or ' ' in object_id):
                raise ValueError('Object ID cannot contain fullstops or spaces: ' + str(object_id))
            obj_id = object_id
            class_id = None
        elif isinstance(object_id, ObjectID):
            obj_id = object_id.object_id
            class_id = object_id.class_id
        else:
            obj_id = None
            class_id = None

        if id_parent is not None:
            self.element_ids = id_parent.element_ids.copy()
            self.element_ids.append(element_id)

            self.class_ids = id_parent.class_ids.copy()
            self.class_ids.append(class_id)

            self.object_ids = id_parent.object_ids.copy()
            self.object_ids.append(obj_id)
        else:
            self.element_ids = [element_id]
            self.class_ids = [class_id]
            self.object_ids = [obj_id]

        self.combined_element_ids = self.ui_manager.get_theme().build_all_combined_ids(
            self.element_ids,
            self.class_ids,
            self.object_ids)
        if self.combined_element_ids is not None and len(self.combined_element_ids) > 0:
            self.most_specific_combined_id = self.combined_element_ids[0]
        else:
            self.most_specific_combined_id = 'no_id'
