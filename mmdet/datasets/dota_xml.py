
from .registry import DATASETS
from .xml_style import XMLDataset


@DATASETS.register_module
class DotaXMLDataset(XMLDataset):

    CLASSES = ('plane', 'baseball-diamond', 'bridge', 'ground-track-field', 'small-vehicle', 'large-vehicle', 
               'ship', 'tennis-court','basketball-court', 'storage-tank',  'soccer-ball-field', 'roundabout', 
               'harbor', 'swimming-pool', 'helicopter','container-crane')