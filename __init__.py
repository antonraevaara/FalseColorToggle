bl_info = {
    "name": "False Color Toggle",
    "author": "Studio Demo",
    "version": (1, 1, 0),
    "blender": (4, 5, 0),
    "location": "View3D",
    "description": "Toggle between selected view transform and False Color",
    "category": "Render",
    "doc_url": "",
    "tracker_url": "",
}

import bpy
from bpy.props import StringProperty, EnumProperty, BoolProperty
from bpy.types import Operator, AddonPreferences


# --- Operator ---------------------------------------------------------------

class VIEW3D_OT_toggle_false_color(Operator):
    """Toggle between selected view transform and False Color"""
    bl_idname = "view3d.toggle_false_color"
    bl_label = "Toggle False Color"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        view_settings = scene.view_settings
        current_transform = view_settings.view_transform

        # Get addon preferences
        prefs = context.preferences.addons[__name__].preferences

        # Get the selected base view transform from preferences
        selected_transform = prefs.selected_view_transform

        if not selected_transform:
            self.report({'WARNING'}, "Please select a view transform in addon preferences")
            return {'CANCELLED'}

        # Toggle: False Color <-> selected transform
        if current_transform == 'False Color':
            view_settings.view_transform = selected_transform
            self.report({'INFO'}, f"Switched to {selected_transform}")
        else:
            view_settings.view_transform = 'False Color'
            self.report({'INFO'}, "Switched to False Color")

        return {'FINISHED'}


# --- Keymap helpers ---------------------------------------------------------

addon_keymaps = []


def _unregister_keymap():
    """Remove previously registered keymaps for this addon."""
    if not addon_keymaps:
        return
    try:
        for km, kmi in addon_keymaps:
            km.keymap_items.remove(kmi)
    except:
        pass
    addon_keymaps.clear()


def _register_keymap():
    """Register keymap based on current preferences."""
    _unregister_keymap()

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon if wm else None
    if not kc:
        return

    try:
        prefs = bpy.context.preferences.addons[__name__].preferences
    except Exception:
        return

    km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
    kmi = km.keymap_items.new(
        VIEW3D_OT_toggle_false_color.bl_idname,
        type=prefs.shortcut_key,
        value="PRESS",
        ctrl=prefs.shortcut_ctrl,
        shift=prefs.shortcut_shift,
        alt=prefs.shortcut_alt,
    )
    addon_keymaps.append((km, kmi))


def _update_shortcut(self, context):
    """Update callback when shortcut settings change in preferences."""
    _register_keymap()


# --- Preferences ------------------------------------------------------------

class FalseColorTogglePreferences(AddonPreferences):
    """Preferences for False Color Toggle addon"""
    bl_idname = __name__

    # Base transform to pair with False Color
    selected_view_transform: EnumProperty(
        name="Base View Transform",
        description="View transform to toggle with False Color",
        items=[
            ('Standard', "Standard", "Standard view transform"),
            ('Filmic', "Filmic", "Filmic view transform"),
            ('Filmic Log', "Filmic Log", "Filmic Log view transform"),
            ('Raw', "Raw", "Raw view transform"),
            ('AgX', "AgX", "AgX view transform"),
        ],
        default='Standard',
    )

    # Shortcut configuration
    shortcut_key: EnumProperty(
        name="Key",
        description="Keyboard key for the toggle shortcut",
        items=[
            ('F1', "F1", ""),
            ('F2', "F2", ""),
            ('F3', "F3", ""),
            ('F4', "F4", ""),
            ('F5', "F5", ""),
            ('F6', "F6", ""),
            ('F7', "F7", ""),
            ('F8', "F8", ""),
            ('F9', "F9", ""),
            ('F10', "F10", ""),
            ('F11', "F11", ""),
            ('F12', "F12", ""),
            ('V', "V", "V key"),
        ],
        default='F8',
        update=_update_shortcut,
    )

    shortcut_ctrl: BoolProperty(
        name="Ctrl",
        default=False,
        update=_update_shortcut,
    )

    shortcut_shift: BoolProperty(
        name="Shift",
        default=False,
        update=_update_shortcut,
    )

    shortcut_alt: BoolProperty(
        name="Alt",
        default=False,
        update=_update_shortcut,
    )

    def draw(self, context):
        layout = self.layout

        # Base transform selection
        box = layout.box()
        box.label(text="View Transform", icon='RENDER_RESULT')
        box.prop(self, "selected_view_transform")
        box.label(text="Toggle: Base transform \u2194 False Color")

        # Shortcut UI
        box = layout.box()
        box.label(text="Toggle Shortcut")
        row = box.row(align=True)
        row.prop(self, "shortcut_ctrl")
        row.prop(self, "shortcut_shift")
        row.prop(self, "shortcut_alt")
        box.prop(self, "shortcut_key")
        box.label(text="Changes apply immediately (3D View).")


# --- Registration -----------------------------------------------------------

def register():
    print("Registering False Color Toggle addon...")
    try:
        bpy.utils.register_class(FalseColorTogglePreferences)
        bpy.utils.register_class(VIEW3D_OT_toggle_false_color)
        _register_keymap()
        print("False Color Toggle addon registered successfully")
    except Exception as e:
        print(f"Error registering False Color Toggle addon: {e}")
        return


def unregister():
    _unregister_keymap()
    bpy.utils.unregister_class(VIEW3D_OT_toggle_false_color)
    bpy.utils.unregister_class(FalseColorTogglePreferences)


if __name__ == "__main__":
    register()
