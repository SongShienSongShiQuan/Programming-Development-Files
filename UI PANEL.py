import bpy


class LayoutDemoPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "NOTE AREA"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    

    def draw(self, context):
        layout = self.layout

        scene = context.scene

        # Create a simple row.
        layout.label(text=" Phyton Test Space")
        row = layout.row()
        row.label(text= "Add a specific object: Cube Mesh", icon= 'CUBE')
        row = layout.row()
        row.operator("mesh.primitive_cube_add")
        
        # bpy.ops.mesh.primitive_plane_add(location=(5,1,3) Add objects using console with location
        
        #Traceback (most recent call last):
  #File "C:\Users\Chowfer\Desktop\T6\Main Files (1)\Blender Files\Phyton Test Space.blend\UI PANEL.py", line 22, in draw
#TypeError: UILayout.operator(): was called with invalid keyword argument(s) (location), expected (operator, text, text_ctxt, translate, icon, emboss, depress, icon_value)



        



def register():
    bpy.utils.register_class(LayoutDemoPanel)


def unregister():
    bpy.utils.unregister_class(LayoutDemoPanel)


if __name__ == "__main__":
    register()