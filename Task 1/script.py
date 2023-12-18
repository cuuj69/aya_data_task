#!/usr/bin/python3

import json

"""visualize the json file using an online tool: online json viewer

map the schema of the client_format and internal_format.json

"""

"""client_format structure overview

-{}Json
 -{}inputRecord
 -{}data
   -{}boxes
   -{}inputData
 -{}resultData
  -{}boxes
    -[]frames(containing 59 arrays 0 being the first)
     -{} 0
       -[]entities
        -{}0
         -[]keyframesType
         -[]relationships
          -{}0
 -{}inputData  


"""

"""inter_format structure overview

-{}JSON
 -{}item
  -{}source_info
   -{}dataset
   -{}team
  -[]slots
   -{}0
    -[]source_files
     -{}0
    -[]frame_urls
 -[]annotations(contains an array of 11 dictionaries of which 0 is part)
  -{}0
   -{}frame(contains 58 more dicts of which 0 is part)
    -{}0
     -{}bounding_box
     -{}instance_id
   -[]ranges
    -[]0
   -[]slot_names
"""

import json

def internal_to_client(internal_data):
    client_frames = []

    annotations = internal_data.get('annotations', [])
    for annotation in annotations:
        frames = annotation.get('frame', [])
        for frame in frames:
            client_frames.append({
                'entities': frame.get('bounding_box', []),
            })

    client_data = {
        'inputRecord': {
            'data': {
                'boxes': {
                    'frames': client_frames
                },
                'inputData': internal_data.get('inputData', {})
            }
        },
        'resultData': {
            'boxes': {
                'frames': client_frames
            }
        }
    }

    return client_data

def client_to_internal(client_data):
    internal_annotations = []

    frames = client_data.get('inputRecord', {}).get('data', {}).get('boxes', {}).get('frames', [])
    for client_frame in frames:
        internal_frame = {
            'bounding_box': client_frame.get('entities', []),
    
        }
        internal_annotation = {'frame': [internal_frame]}
        internal_annotations.append(internal_annotation)

    internal_data = {
        'JSON': {
            'item': {
                'source_info': {
                    'dataset': '',
                    'team': ''
                }
            },
            'annotations': internal_annotations
        }
    }

    return internal_data

def convert_internal_to_client(input_file='internal_format.json', output_file='client_format.json'):
    with open(input_file, 'r') as internal_file:
        internal_data = json.load(internal_file)

    client_data = internal_to_client(internal_data)

    with open(output_file, 'w') as client_file:
        json.dump(client_data, client_file, indent=2)

def convert_client_to_internal(input_file='client_format.json', output_file='internal_format.json'):
    with open(input_file, 'r') as client_file:
        client_data = json.load(client_file)

    internal_data = client_to_internal(client_data)

    with open(output_file, 'w') as internal_file:
        json.dump(internal_data, internal_file, indent=2)

#to_client
convert_internal_to_client()

#to_internal
convert_client_to_internal()
























































































































































