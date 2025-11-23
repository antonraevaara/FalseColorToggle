## False Color Toggle (Blender 4.5+)

Toggle between a chosen View Transform and **False Color** with a single shortcut in the 3D Viewport.

1.	Download the ZIP:
https://github.com/antonraevaara/FalseColorToggle/raw/refs/heads/main/FalseColorToggle.zip￼

2.	In Blender:
Edit → Preferences → Add-ons → Install…
Select the ZIP and enable False Color Toggle.


This is version 1.1, so the feature set is still limited.
Shortcut options are restricted to F-keys (F1–F12) combined with Ctrl / Shift / Alt.
Let me know if you need more options in the next version.


---------------------------



### Features

- **Toggle**: Base View Transform ↔ False Color
- **Supports**: Standard, Filmic, Filmic Log, Raw, AgX
- **User-configurable shortcut** (key + Ctrl/Shift/Alt) directly in Add-on preferences
- **Single-file add-on** (`__init__.py`), no external dependencies

### Requirements

- Blender **4.5** or newer
- Color management configuration that provides the **False Color** view (default in Blender 4.5+)

### Configuration

1. Open: `Edit → Preferences → Add-ons → False Color Toggle`
2. **Base View Transform**:
   - Choose which view transform (e.g. `AgX`, `Filmic`, `Standard`) you want to pair with False Color.
3. **Toggle Shortcut**:
   - Choose modifiers (**Ctrl / Shift / Alt**) and a **Key** (F1–F12).
   - Changes are applied immediately to the `3D View` keymap.

### Usage

- In a 3D Viewport, press your configured shortcut:
  - If the current view transform is **False Color** → it switches to the selected **Base View Transform**
  - Otherwise → it switches to **False Color**

### Development

- **Entry point**: `__init__.py`
- **Operator**: `view3d.toggle_false_color`
- **Preferences class**: `FalseColorTogglePreferences`
  - Stores the base view transform selection and shortcut
  - Registers/updates the keymap automatically

### License

This add-on is intended to be distributed under a free/open-source license.  
A suitable choice for the Blender ecosystem is e.g. **GPL-3.0-or-later** or another GPL-compatible license.


