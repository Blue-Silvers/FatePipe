import pathlib

templates = {
    "asset": {"glob": "Asset",
                   "regex": 'Asset',
                   },

    "asset_type" : {"glob": "Asset/{asset_type}",
                    "regex": 'Asset/(?P<asset_type>.*)',
                    },
    "asset_name" : {"glob": "Asset/{asset_type}/{asset_name}",
                    "regex": 'Asset/(?P<asset_type>.*)/(?P<asset_name>.*)',
                    },
    "asset_task": {"glob": "Asset/{asset_type}/{asset_name}/{asset_task}",
                   "regex": 'Asset/(?P<asset_type>.*)/(?P<asset_name>.*)/(?P<asset_task>.*)',
                   },
    "asset_version": {"glob": "Asset/{asset_type}/{asset_name}/{asset_task}/{asset_version}",
                   "regex": 'Asset/(?P<asset_type>.*)/(?P<asset_name>.*)/(?P<asset_task>.*)/(?P<asset_version>.*)',
                   },
    "asset_item": {"glob": "Asset/{asset_type}/{asset_name}/{asset_task}/{asset_version}/{asset_item}",
                      "regex": 'Asset/(?P<asset_type>.*)/(?P<asset_name>.*)/(?P<asset_task>.*)/(?P<asset_version>.*)/(?P<asset_item>.*)',
                      },

    "shot": {"glob": "Shot/Ep001/",
                  "regex": 'Shot/Ep001/',
             },

    "shot_type": {"glob": "Shot/Ep001/{shot_type}",
                   "regex": 'Shot/Ep001/(?P<shot_type>.*)',
                   },
    "shot_name": {"glob": "Shot/Ep001/{shot_type}/{shot_name}",
                   "regex": 'Shot/Ep001/(?P<shot_type>.*)/(?P<shot_name>.*)',
                   },
    "shot_task": {"glob": "Shot/Ep001/{shot_type}/{shot_name}/{shot_task}",
                   "regex": 'Shot/Ep001/(?P<shot_type>.*)/(?P<shot_name>.*)/(?P<shot_task>.*)',
                   },
    "shot_version": {"glob": "Shot/Ep001/{shot_type}/{shot_name}/{shot_task}/{shot_version}",
                      "regex": 'Shot/Ep001/(?P<shot_type>.*)/(?P<shot_name>.*)/(?P<shot_task>.*)/(?P<shot_version>.*)',
                      },
    "shot_item": {"glob": "Shot/Ep001/{shot_type}/{shot_name}/{shot_task}/{shot_version}/{shot_item}",
                   "regex": 'Shot/Ep001/(?P<shot_type>.*)/(?P<shot_name>.*)/(?P<shot_task>.*)/(?P<shot_version>.*)/(?P<shot_item>.*)',
                   },
}

folderTemplates = {
    "asset": {"name": ["Model", "Rig", "Texture"],
                    "task": ["v010"],
                    "version": ["Publish", "Work"],
              },
    "asset_type": {
                    "task": ["v010"],
                    "version": ["Publish", "Work"],
                   },
    "asset_name" : {
                    "version": ["Publish", "Work"],
                    },
    "asset_task" : {
                    },

    "shot": {
                "name": ["Sh010"],
                "task": ["Animation", "Compositing", "Lighting", "Rendering"],
                "version": ["Publish", "Work"],
            },
    "shot_type": {
                    "task": ["Animation", "Compositing", "Lighting", "Rendering"],
                    "version": ["Publish", "Work"],
                   },
    "shot_name": {
                    "version": ["Publish", "Work"],
                   },
    "shot_task": {
                   },
}

root = (pathlib.Path(__file__).parent.parent.parent.parent /"fileExplorer"/"Root").resolve(True)
print(root)