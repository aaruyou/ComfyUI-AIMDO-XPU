"""
comfy_aimdo.malloc_graph - XPU compatibility layer

ComfyUI imports this module unconditionally, but malloc graphs are
CUDA-specific in the current ComfyUI implementation.

AIMDO-XPU uses Intel XPU and therefore provides a safe no-op API here.
"""

from contextlib import nullcontext
from weakref import WeakSet


_comfy_active = False
_comfy_cuda_graph_modules = WeakSet()


class MallocGraph:
    """
    XPU-safe no-op replacement for comfy_aimdo.malloc_graph.MallocGraph.
    """

    def __init__(self):
        self._comfy_active = False
        self._comfy_cuda_graph_modules = WeakSet()
        self.rogue_count = 0

    def push(self):
        return None

    def pop(self):
        return False

    def abort(self):
        return None

    def pause(self, sync=False):
        return None

    def resume(self, sync=False):
        return None

    def iterate(self, scope=None):
        return False

    def use_stream(self, stream):
        return nullcontext()

    def destroy(self):
        return None


def record(stream, assert_graph_breaks=False):
    """
    Return an XPU-safe no-op malloc graph object.

    This should not normally be reached for XPU because
    ComfyUI's malloc_graph_enabled() rejects non-CUDA devices.
    """
    return MallocGraph()


def pause():
    return None


def resume():
    return None


def iterate(scope=None):
    return False


def use_stream(stream):
    return nullcontext()
