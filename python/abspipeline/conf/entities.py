

templates = {
    "asset_type" : {"glob": "Asset/{asset_type}",
                    "regex": 'Asset/(?P<asset_type>.*)',
                    },
    "asset_name" : {"glob": "Asset/{asset_type}/{asset_name}",
                    "regex": 'Asset/(?P<asset_type>.*)/(?P<asset_name>.*)',
                    },
}

root = "C:/Users/enzo.lahana/PycharmProjects/FatePipe/fileExplorer/Task"
