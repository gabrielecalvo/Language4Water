from shapely.geometry import MultiPolygon

def ensure_mutipoly(x):
    return [MultiPolygon([i]) if not isinstance(i, MultiPolygon) else i for i in x]