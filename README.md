# About
This is a clone of the Blender add-ons repo, modified to fit internal
use cases at POET Industries. It contains additional add-ons as well
as modifications to existing ones. It should be installed on top of
the existing add-ons directory.

## Additional Add-ons
- Root Motionist

## Modified Add-ons
- FBX Format

## Changes from previous version
- FBX exporter exports meshes after sorting them alphabetically. This lets
  users define the order of material slots on the exported file. Having
  control of this order is important in cases where the rendering order depends
  on the material layout of rendered meshes. An example of this is Unreal
  Engine 4, where translucent sorting of DBuffer decals on the same mesh
  happens according to the material slot position inside that mesh.
- UV Magic has been removed since it is part of the official Blender addon
  repository starting with Blender 2.79.
