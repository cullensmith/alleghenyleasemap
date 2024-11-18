from django.shortcuts import render
from .models import Wells_C
from .models import Wells_U
from .models import Parcels
from .models import Points
from .models import PolygonModel
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models.functions import Substr
from django.core.cache import cache

from django.db.models import Q
import json 
import ast




def leasemap(request):
    return render(request, 'leasemap.html')

def getMask(request):
    themask = {
        "type": "FeatureCollection",
        "name": "county_mask",
        "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
        "features": [
        { "type": "Feature", "properties": { "id": 1 }, "geometry": { "type": "MultiPolygon", "coordinates": [ [ [ [ -69.609811018786672, 46.606528718408548 ], [ -69.53563960003703, 31.821692580977391 ], [ -87.732360999952292, 32.241997287225431 ], [ -87.114265843705169, 46.631252524658436 ], [ -69.609811018786672, 46.606528718408548 ] ], [ [ -80.360873, 40.477539 ], [ -80.31071, 40.437124 ], [ -80.310055, 40.436436 ], [ -80.296579, 40.425446 ], [ -80.287991, 40.418484 ], [ -80.286407, 40.41754 ], [ -80.273381, 40.407234 ], [ -80.272086, 40.406019 ], [ -80.258865, 40.395241 ], [ -80.2347, 40.375368 ], [ -80.234373, 40.375045 ], [ -80.228053, 40.369957 ], [ -80.223067, 40.365826 ], [ -80.183462, 40.332774 ], [ -80.182285, 40.33224 ], [ -80.171147, 40.328899 ], [ -80.161507, 40.325941 ], [ -80.145933, 40.321276 ], [ -80.123296, 40.31448 ], [ -80.116156, 40.312324 ], [ -80.095612, 40.306184 ], [ -80.094945, 40.305907 ], [ -80.077004, 40.300756 ], [ -80.07396, 40.299837 ], [ -80.072297, 40.299348 ], [ -80.069255, 40.298589 ], [ -80.047252, 40.291859 ], [ -80.033712, 40.288034 ], [ -80.0331, 40.287848 ], [ -80.017342, 40.283029 ], [ -80.00278, 40.278677 ], [ -79.974254, 40.270289 ], [ -79.973309, 40.269935 ], [ -79.969083, 40.268662 ], [ -79.943541, 40.261361 ], [ -79.940484, 40.260416 ], [ -79.922084, 40.254894 ], [ -79.921028, 40.254528 ], [ -79.919166, 40.253961 ], [ -79.918005, 40.253696 ], [ -79.914139, 40.252518 ], [ -79.916379, 40.24999 ], [ -79.922955, 40.24615 ], [ -79.928347, 40.243782 ], [ -79.934946, 40.242058 ], [ -79.939963, 40.241494 ], [ -79.953788, 40.240774 ], [ -79.95942, 40.23975 ], [ -79.964764, 40.23767 ], [ -79.966076, 40.236918 ], [ -79.9691, 40.234278 ], [ -79.970428, 40.232246 ], [ -79.97094, 40.229718 ], [ -79.97021, 40.226379 ], [ -79.968335, 40.22382 ], [ -79.963612, 40.219462 ], [ -79.959532, 40.216134 ], [ -79.956073, 40.213582 ], [ -79.954406, 40.212778 ], [ -79.950382, 40.211559 ], [ -79.938683, 40.209814 ], [ -79.927883, 40.206822 ], [ -79.925657, 40.205859 ], [ -79.92155, 40.203195 ], [ -79.918346, 40.200555 ], [ -79.916056, 40.199453 ], [ -79.912586, 40.197767 ], [ -79.909082, 40.196823 ], [ -79.900246, 40.195095 ], [ -79.896448, 40.194481 ], [ -79.893402, 40.194343 ], [ -79.888986, 40.194823 ], [ -79.881913, 40.196519 ], [ -79.876265, 40.197175 ], [ -79.870585, 40.197415 ], [ -79.83908, 40.20845 ], [ -79.816989, 40.215779 ], [ -79.783747, 40.227046 ], [ -79.78259, 40.227358 ], [ -79.781761, 40.227711 ], [ -79.787364, 40.227994 ], [ -79.789149, 40.22908 ], [ -79.795637, 40.230107 ], [ -79.804536, 40.232101 ], [ -79.806002, 40.233205 ], [ -79.807046, 40.235764 ], [ -79.806997, 40.237524 ], [ -79.805015, 40.241106 ], [ -79.803331, 40.241609 ], [ -79.798463, 40.247715 ], [ -79.796099, 40.253365 ], [ -79.790401, 40.258812 ], [ -79.788722, 40.260261 ], [ -79.787542, 40.263246 ], [ -79.788779, 40.265312 ], [ -79.795221, 40.272368 ], [ -79.796241, 40.276037 ], [ -79.796515, 40.279183 ], [ -79.795771, 40.281073 ], [ -79.794715, 40.281683 ], [ -79.790678, 40.282217 ], [ -79.781199, 40.281966 ], [ -79.777781, 40.283361 ], [ -79.775829, 40.284984 ], [ -79.774923, 40.286489 ], [ -79.775139, 40.287888 ], [ -79.775963, 40.28921 ], [ -79.779522, 40.292665 ], [ -79.786173, 40.29695 ], [ -79.787853, 40.297693 ], [ -79.785946, 40.307604 ], [ -79.784208, 40.313894 ], [ -79.783806, 40.315441 ], [ -79.783332, 40.317251 ], [ -79.782067, 40.323269 ], [ -79.781851, 40.323845 ], [ -79.778044, 40.34126 ], [ -79.774412, 40.359673 ], [ -79.773492, 40.363527 ], [ -79.771059, 40.374053 ], [ -79.771082, 40.375419 ], [ -79.765943, 40.384188 ], [ -79.763383, 40.385547 ], [ -79.764322, 40.386512 ], [ -79.765137, 40.389468 ], [ -79.762068, 40.392768 ], [ -79.758609, 40.392064 ], [ -79.753776, 40.388538 ], [ -79.751262, 40.388357 ], [ -79.751004, 40.389076 ], [ -79.750529, 40.391124 ], [ -79.747748, 40.391041 ], [ -79.744702, 40.3959 ], [ -79.742201, 40.396916 ], [ -79.738522, 40.395713 ], [ -79.738692, 40.39791 ], [ -79.736422, 40.399391 ], [ -79.734942, 40.397858 ], [ -79.732528, 40.399536 ], [ -79.73232, 40.400235 ], [ -79.732195, 40.406003 ], [ -79.730345, 40.408465 ], [ -79.729967, 40.408668 ], [ -79.727768, 40.408267 ], [ -79.722365, 40.408689 ], [ -79.722151, 40.409098 ], [ -79.725677, 40.41191 ], [ -79.727665, 40.412495 ], [ -79.727467, 40.412868 ], [ -79.72645, 40.414232 ], [ -79.722338, 40.414919 ], [ -79.720423, 40.413982 ], [ -79.717698, 40.413664 ], [ -79.715987, 40.417319 ], [ -79.712545, 40.418647 ], [ -79.71188, 40.419648 ], [ -79.707042, 40.422426 ], [ -79.706734, 40.424596 ], [ -79.705092, 40.4262 ], [ -79.70473, 40.427562 ], [ -79.703834, 40.443526 ], [ -79.703394, 40.455945 ], [ -79.703083, 40.463577 ], [ -79.702485, 40.477326 ], [ -79.702142, 40.489523 ], [ -79.702264, 40.517891 ], [ -79.701985, 40.523787 ], [ -79.701624, 40.525449 ], [ -79.705101, 40.527111 ], [ -79.707902, 40.530663 ], [ -79.710234, 40.532299 ], [ -79.712844, 40.532872 ], [ -79.714638, 40.533166 ], [ -79.718682, 40.537407 ], [ -79.720859, 40.541 ], [ -79.722424, 40.542059 ], [ -79.724567, 40.542366 ], [ -79.729786, 40.54416 ], [ -79.73061, 40.544819 ], [ -79.732351, 40.545515 ], [ -79.735938, 40.549176 ], [ -79.739343, 40.549543 ], [ -79.742639, 40.548718 ], [ -79.745023, 40.549491 ], [ -79.748228, 40.551181 ], [ -79.752385, 40.551574 ], [ -79.753976, 40.550538 ], [ -79.758132, 40.550337 ], [ -79.760995, 40.55103 ], [ -79.765415, 40.549854 ], [ -79.765946, 40.550915 ], [ -79.77187, 40.562967 ], [ -79.77437, 40.569767 ], [ -79.773331, 40.580758 ], [ -79.772285, 40.583788 ], [ -79.770371, 40.586366 ], [ -79.764001, 40.592735 ], [ -79.76377, 40.592966 ], [ -79.75747, 40.595966 ], [ -79.749187, 40.59897 ], [ -79.74117, 40.600666 ], [ -79.733169, 40.603135 ], [ -79.728579, 40.604774 ], [ -79.72127, 40.607966 ], [ -79.717081, 40.613352 ], [ -79.715738, 40.616494 ], [ -79.712807, 40.619873 ], [ -79.712477, 40.620076 ], [ -79.710343, 40.621031 ], [ -79.702691, 40.626023 ], [ -79.699579, 40.629008 ], [ -79.69378, 40.635276 ], [ -79.690837, 40.639234 ], [ -79.689117, 40.642722 ], [ -79.688777, 40.644385 ], [ -79.688986, 40.648705 ], [ -79.690842, 40.653329 ], [ -79.695226, 40.660321 ], [ -79.695594, 40.664193 ], [ -79.694523, 40.666256 ], [ -79.692475, 40.668069 ], [ -79.69251, 40.669156 ], [ -79.692587, 40.669732 ], [ -79.69293, 40.669744 ], [ -79.694474, 40.669649 ], [ -79.698705, 40.669726 ], [ -79.707546, 40.669851 ], [ -79.717121, 40.669656 ], [ -79.731924, 40.669241 ], [ -79.743643, 40.669777 ], [ -79.745508, 40.669679 ], [ -79.760108, 40.670449 ], [ -79.76414, 40.670497 ], [ -79.786358, 40.671543 ], [ -79.811838, 40.672255 ], [ -79.816997, 40.671753 ], [ -79.825406, 40.671201 ], [ -79.828636, 40.671073 ], [ -79.83236, 40.671394 ], [ -79.866027, 40.672264 ], [ -79.87713, 40.672309 ], [ -79.888737, 40.672642 ], [ -79.914627, 40.673232 ], [ -79.916033, 40.67309 ], [ -79.924182, 40.673021 ], [ -79.96077, 40.672306 ], [ -79.963407, 40.672408 ], [ -79.964595, 40.672514 ], [ -79.977043, 40.673042 ], [ -79.987842, 40.673587 ], [ -79.99418, 40.673636 ], [ -79.99517, 40.673635 ], [ -79.996979, 40.673635 ], [ -80.060124, 40.674143 ], [ -80.067531, 40.674165 ], [ -80.068355, 40.674167 ], [ -80.071393, 40.674174 ], [ -80.071434, 40.674935 ], [ -80.095724, 40.674179 ], [ -80.11326, 40.673869 ], [ -80.125105, 40.673669 ], [ -80.126088, 40.673695 ], [ -80.148451, 40.67429 ], [ -80.148677, 40.673848 ], [ -80.146629, 40.64314 ], [ -80.146708, 40.642093 ], [ -80.146317, 40.638786 ], [ -80.144907, 40.614771 ], [ -80.145383, 40.613408 ], [ -80.148203, 40.611626 ], [ -80.150696, 40.611884 ], [ -80.152061, 40.60948 ], [ -80.155061, 40.608069 ], [ -80.158602, 40.609172 ], [ -80.160343, 40.609581 ], [ -80.165121, 40.606542 ], [ -80.169081, 40.606363 ], [ -80.169972, 40.607723 ], [ -80.171834, 40.6082 ], [ -80.173344, 40.607792 ], [ -80.176221, 40.6083 ], [ -80.177753, 40.609254 ], [ -80.180333, 40.609233 ], [ -80.180441, 40.607639 ], [ -80.182423, 40.605545 ], [ -80.184151, 40.604439 ], [ -80.184725, 40.602849 ], [ -80.183973, 40.601328 ], [ -80.188384, 40.600105 ], [ -80.188547, 40.599473 ], [ -80.184734, 40.597715 ], [ -80.184753, 40.596856 ], [ -80.186331, 40.596293 ], [ -80.190158, 40.596275 ], [ -80.193143, 40.596865 ], [ -80.194897, 40.596772 ], [ -80.195357, 40.595975 ], [ -80.199098, 40.59239 ], [ -80.201826, 40.591194 ], [ -80.204181, 40.58866 ], [ -80.206793, 40.588225 ], [ -80.207978, 40.588038 ], [ -80.208529, 40.586722 ], [ -80.21082, 40.585417 ], [ -80.211832, 40.582484 ], [ -80.214231, 40.580883 ], [ -80.218002, 40.581804 ], [ -80.218756, 40.582027 ], [ -80.219175, 40.579453 ], [ -80.220229, 40.579885 ], [ -80.224142, 40.577117 ], [ -80.22436, 40.575234 ], [ -80.228579, 40.573072 ], [ -80.233369, 40.569578 ], [ -80.251491, 40.556059 ], [ -80.263694, 40.547257 ], [ -80.272578, 40.541045 ], [ -80.274376, 40.539373 ], [ -80.275125, 40.538767 ], [ -80.278026, 40.536736 ], [ -80.342272, 40.49089 ], [ -80.360782, 40.477604 ], [ -80.360873, 40.477539 ] ] ] ] } }
        ]
        }

    print('getting the mask ready')
    return JsonResponse(themask)


def polygon_geojson_view(request):
    # Try to get the cached response
    cache_key = 'polygons_geojson'
    cached_data = cache.get(cache_key)

    if cached_data:
        # print(f'found the cache: {time.time()-start_time}')
        print('resorting to the cache')
        return JsonResponse(cached_data, safe=False)


    polygons = PolygonModel.objects.all()  # Query all polygons
    features = []
    for i,polygon in enumerate(polygons):
        # if i > 5:
        #     break
        # Parse GeoJSON text from the geomjson field
        geojson_data = polygon.geomjson
        # Add GeoJSON feature to the list
        feature = dict()
        feature['type'] = "Feature"
        feature['properties'] = polygon.pin
        feature['geometry'] = ast.literal_eval(geojson_data)
        features.append(feature)
        # print('so we got here')
        
    # Create GeoJSON FeatureCollection
    geojson_collection = {
        "type": "FeatureCollection",
        "features": features
    }
    # print(geojson_collection)
    print('requested polygons')
    cache.set(cache_key, geojson_collection, timeout=60*1440)  # Cache for 15 minutes

    return JsonResponse(geojson_collection, safe=False)

def get_wellsc(request):
    pts = Wells_C.objects.all()  # Query all polygons
    features = []
    for i,pt in enumerate(pts):
        # if i > 5:
        #     break
        # Parse GeoJSON text from the geomjson field
        geojson_data = pt.geomjson
        # Add GeoJSON feature to the list
        feature = dict()
        feature['type'] = "Feature"
        feature['properties'] = pt.permit_num
        feature['geometry'] = ast.literal_eval(geojson_data)
        features.append(feature)
        # print('so we got here')
        
    # Create GeoJSON FeatureCollection
    geojson_collection = {
        "type": "FeatureCollection",
        "features": features
    }
    # print(geojson_collection)
    print('requested conventional')
    return JsonResponse(geojson_collection)

def get_wellsu(request):
    pts = Wells_U.objects.all()  # Query all polygons
    features = []
    for i,pt in enumerate(pts):
        # if i > 5:
        #     break
        # Parse GeoJSON text from the geomjson field
        geojson_data = pt.geomjson
        # Add GeoJSON feature to the list
        feature = dict()
        feature['type'] = "Feature"
        feature['properties'] = pt.permit_num
        feature['geometry'] = ast.literal_eval(geojson_data)
        features.append(feature)
        # print('so we got here')
        
    # Create GeoJSON FeatureCollection
    geojson_collection = {
        "type": "FeatureCollection",
        "features": features
    }
    # print(geojson_collection)
    print('requested unconventional')
    return JsonResponse(geojson_collection)

def filteredparcels(request):
    print('grabbing filtered parcels')
    print(request)
    print(request.GET.getlist('zoning'))
    print(request.GET.getlist('schools'))
    agmt_in = request.GET.getlist('agmt')[0].split(',')
    company_in = request.GET.getlist('company')[0].split(',')
    munis_in = request.GET.getlist('munis')[0].split(',')
    schools_in = request.GET.getlist('schools')[0].split(',')
    zoning_in = request.GET.getlist('zoning')[0].split(',')
    # print(f'schools = {schools_in}')
    a = list()
    for s in agmt_in:
        h = s.strip()
        # states.append(h)
        # states.append(h.upper())
        # states.append(h.lower())
        a.append(h)
    cl = list()
    for s in company_in:
        h = s.strip()
        # states.append(h)
        # states.append(h.upper())
        # states.append(h.lower())
        cl.append(h)
    md = list()
    for s in munis_in:
        h = s.strip()
        # states.append(h)
        # states.append(h.upper())
        # states.append(h.lower())
        md.append(s)
    sd = list()
    for s in schools_in:
        h = s.strip()
        # states.append(h)
        # states.append(h.upper())
        # states.append(h.lower())
        sd.append(h.title())
    # print(f'school districts = {schools_in}')
    zoning = list()
    for s in zoning_in:
        h = s.strip()
        # states.append(h)
        # states.append(h.upper())
        # states.append(h.lower())
        zoning.append(h.upper())
    print(f"company--{len(cl)}->{cl}")
    print(f"muni--{len(md)}->{md}")
    print(f"school--{len(sd)}->{sd}")
    print(f"zoning--{len(zoning)}->{zoning}")

    print(f"zoning--{len(zoning)}->{zoning}")
    filter_kwargs = dict()
    filter_kwargs.update({'agmt_type__in':a})
    filter_kwargs.update({'company__in':cl})
    filter_kwargs.update({'munidesc__in':md})
    filter_kwargs.update({'schooldesc__in':sd})
    filter_kwargs.update({'classdesc__in':zoning})
    polygons = Parcels.objects.filter(**filter_kwargs)
    print('here there are')
    print(polygons)
    print('we get any?')
    print(len(set(polygons)))
    features = []


    for i,polygon in enumerate(set(polygons)):
        # if i > 5:
        #     break
        # Parse GeoJSON text from the geomjson field
        geojson_data = polygon.geomjson
        # Add GeoJSON feature to the list
        feature = dict()
        feature['type'] = "Feature"
        feature['properties'] = polygon.pin
        feature['geometry'] = ast.literal_eval(geojson_data)
        features.append(feature)
        # print('so we got here')
        
    # Create GeoJSON FeatureCollection
    geojson_collection = {
        "type": "FeatureCollection",
        "features": features
    }
    # print(geojson_collection)
    print('requested polygons')
    return JsonResponse(geojson_collection)

def get_matches(request):
    print('grabbing filtered pins')
    print(request)
    p = request.GET.getlist('pin')[0]
    polygons = Parcels.objects.filter(Q(pin = p))
    # for r in polygons:
    #     print(f'doc number: {r.doc_num}, deed url: {r.dv_url}')
    # print('those were it')
    # return JsonResponse({"text": "here is the new text"})
    features = []
    for i,polygon in enumerate(polygons.annotate(last_four=Substr('file_date',8,3)).order_by('-last_four')):
        # if i > 5:
        #     break
        # Parse GeoJSON text from the geomjson field
        geojson_data = polygon.geomjson
        # Add GeoJSON feature to the list
        feature = dict()
        feature['type'] = "Feature"
        feature['pin'] = polygon.pin
        feature['doc_num'] = polygon.doc_num
        feature['company'] = polygon.company
        feature['file_date'] = polygon.file_date
        feature['agmt_type'] = polygon.agmt_type
        feature['munidesc'] = polygon.munidesc
        feature['bk_vol_pg'] = polygon.bk_vol_pg
        feature['schooldesc'] = polygon.schooldesc
        feature['classdesc'] = polygon.classdesc
        feature['fairmarkettotal'] = polygon.fairmarkettotal
        feature['calcacreag'] = polygon.calcacreag
        feature['usedesc'] = polygon.usedesc
        feature['dv_url'] = polygon.dv_url
        feature['geometry'] = ast.literal_eval(geojson_data)
        features.append(feature)
        # print('so we got here')
        
    # Create GeoJSON FeatureCollection
    geojson_collection = {
        "type": "FeatureCollection",
        "features": features
    }
    # print(geojson_collection)
    print('requested polygons')
    return JsonResponse(geojson_collection)

def parcels(request):
    print('grabbing parcels')
    polygons = Parcels.objects.all()
    polygons_data = []

    for polygon in polygons:
        # print(f'parcel---> {polygon}')
        polygon_data = {
            'company': polygon.field_2,
            'record_type': polygon.field_5,
            'municipality': polygon.propertycity,
            'zoning': polygon.classdesc,
            'geometry': polygon.geomjson
        }
        polygons_data.append(polygon_data)
    print('got the parcel data')
    geojson = {
        "type": "FeatureCollection",
        "features": [
        {
            "type": "Feature",
            "geometry" : {
                "type": "MultiPolygon",
                "coordinates": [d["coordinates"]],
                },
            "properties" : d,
        } for d in polygons_data]
    }

    mapdata = json.dumps(geojson)
    return JsonResponse(mapdata, safe=False)






def coordints(request):
    c = request.GET.getlist('coords[]')
    print(f'lat: {c[0]}')
    print(f'lat: {c[1]}')