# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

bl_info = {
    "name": "Quake MAP format",
    "author": "Campbell Barton",
    "blender": (2, 5, 7),
    "api": 35622,
    "location": "File > Export",
    "description": "Export MAP brushes, nurbs surfaces, lamps and empties as map nodes",
    "warning": "",
    "wiki_url": "http://wiki.blender.org/index.php/Extensions:2.5/Py/"\
        "Scripts/Import-Export/Quake_MAP",
    "tracker_url": "",
    "support": 'OFFICIAL',
    "category": "Import-Export"}

# To support reload properly, try to access a package var, if it's there, reload everything
if "bpy" in locals():
    import imp
    if "export_map" in locals():
        imp.reload(export_map)


import bpy
from bpy.props import StringProperty, BoolProperty, FloatProperty, EnumProperty
from bpy_extras.io_utils import ExportHelper, axis_conversion


class ExportMAP(bpy.types.Operator, ExportHelper):
    '''Export selection to a quake map'''
    bl_idname = "export_scene.quake_map"
    bl_label = "Export MAP"
    bl_options = {'PRESET'}

    filename_ext = ".map"
    filter_glob = StringProperty(default="*.map", options={'HIDDEN'})

    def execute(self, context):
        import math
        from mathutils import Matrix
        if not self.filepath:
            raise Exception("filepath not set")

        '''
        global_matrix = Matrix()
        global_matrix[0][0] = global_matrix[1][1] = global_matrix[2][2] = self.global_scale
        global_matrix = global_matrix * axis_conversion(to_forward=self.axis_forward, to_up=self.axis_up).to_4x4()

        keywords = self.as_keywords(ignore=("axis_forward", "axis_up", "global_scale", "check_existing", "filter_glob"))
        keywords["global_matrix"] = global_matrix
        '''

        keywords = self.as_keywords(ignore=("check_existing", "filter_glob"))

        from . import export_map
        return export_map.save(self, context, **keywords)


def menu_func(self, context):
    self.layout.operator(ExportMAP.bl_idname, text="Quake MAP (.map)")


def register():
    bpy.utils.register_module(__name__)

    bpy.types.INFO_MT_file_export.append(menu_func)


def unregister():
    bpy.utils.unregister_module(__name__)

    bpy.types.INFO_MT_file_export.remove(menu_func)

if __name__ == "__main__":
    register()