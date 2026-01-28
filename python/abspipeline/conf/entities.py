import os

templates = {
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
    "asset_type": {
                    #"name": ["Model", "Rig", "Texture"],
                    "task": ["v010"],
                    "version": ["Publish", "Work"],
                   },
    "asset_name" : {
                    "task": ["v010"],
                    "version": ["Publish", "Work"],
                    },
    "asset_task" : {
                    "version": ["Publish", "Work"],
                    },

    "shot_name": {
                    "name": ["Sh010"],
                    "task": ["Animation", "Compositing", "Lighting", "Rendering"],
                    "version": ["Publish", "Work"],
                   },
    "shot_task": {
                    "task": ["Animation", "Compositing", "Lighting", "Rendering"],
                    "version": ["Publish", "Work"],
                   },
    "shot_version": {
                    "version": ["Publish", "Work"],
                   },
}

# root = "C:/Users/enzo.lahana/PycharmProjects/FatePipe/fileExplorer/Task"
#root = "C:/Users/fury8/PycharmProjects/FatePipe/fileExplorer/Task"
#root =  "C:/Users/enzo.lahana/Documents/PycharmProjects/FatePipe/fileExplorer/Task"
root = os.path.join(os.path.dirname(__file__), "../../../fileExplorer/Task")
