#Notes for blender console. Getting data of a mesh
#mako_verts [vert.co for vert in bpy.context.object.data.vertices]
mako_verts = [vert.co for vert in C.object.data.vertices]
#The above line will print the coordinates of mako mesh. If vert.co is vert only. It will print the total number of vertices only.
#type mako_verts to print the vertices
mako_verts #prints the vertices.
#To add the vertices using console D.texts['addon.py'].write("Hi") This will add the "Hi" text to the cursor location in the python script.
D.texts['addon.py'].write("Hi")
bpy.data.texts['addon.py'].write("Hi")
#To add the vertices using console D.texts['addon.py'].write(mako_verts.__repr__()) This will add the "mako_verts" You need to use the function __repr__() to convert the list to string.
D.texts['addon.py'].write(mako_verts.__repr__())
#The code below lists the faces/polygons of a mesh. If you only do o.vertices for o in C.object.data.polygons] it's not yet a list so you need to add a 
# a comprehension inside the comprehension to be able to create a list of the data.
mako_faces = [[vert for vert in o.vertices] for o in C.object.data.polygons]
D.texts['addon.py'].write(mako_faces.__repr__())

#important __repr__() CONVERTS LIST TO STRING TO WRITE THE DATA TO A SCRIPT USING CONSOLE
CTRL + T to view icons in blender
#Go to preferences and add ons to add icon viewer for development