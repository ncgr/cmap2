from os import path
from bokeh.models.layouts import LayoutDOM
from bokeh.core.properties import Instance, List
from bokeh.util.compiler import FromFile

script_path = path.dirname(path.abspath( __file__ ))


class MapSetRenderer(LayoutDOM):
    __implementation__ = FromFile(script_path + '/map_set_renderer.js')
    # feature_locs = List(Instance(FeatureLocation))
