# -*- coding: utf-8 -*-

import datasets
_TRAIN_DOWNLOAD_URL = "https://raw.githubusercontent.com/chriott/tsv-train/main/sample.tsv"
_DEV_DOWNLOAD_URL = "https://raw.githubusercontent.com/chriott/tsv-train/main/dev.tsv"

logger = datasets.logging.get_logger(__name__)
class PosConfig(datasets.BuilderConfig):
    """BuilderConfig for Pos2021"""

    def __init__(self, **kwargs):
        """BuilderConfig for Pos2021.

        Args:
          **kwargs: keyword arguments forwarded to super.
        """
        super(PosConfig, self).__init__(**kwargs)

        
class Pos2021(datasets.GeneratorBasedBuilder):
    BUILDER_CONFIGS = [
        PosConfig(name="Pos2021", version=datasets.Version("1.0.0"), description="Pos2021 dataset"),
    ]  
    def _info(self):
        return datasets.DatasetInfo(
                features=datasets.Features(
                        {
                    #"position": datasets.Sequence(datasets.Value("string")),
                    "tokens": datasets.Sequence(datasets.Value("string")),
                    #"sid": datasets.Value("string"),
                    "pos_tags": datasets.Sequence(
                        datasets.features.ClassLabel(
                            names=[
                                '"',
                                "''",
                                "#",
                                "$",
                                "(",
                                ")",
                                ",",
                                ".",
                                ":",
                                "``",
                                "CC",
                                "CD",
                                "DT",
                                "EX",
                                "FW",
                                "HYPH",
                                "IN",
                                "JJ",
                                "JJR",
                                "JJS",
                                "LS",
                                "-LRB-",
                                "MD",
                                "NN",
                                "NNP",
                                "NNPS",
                                "NNS",
                                "NN|SYM",
                                "PDT",
                                "POS",
                                "PRP",
                                "PRP$",
                                "-RRB-",
                                "RB",
                                "RBR",
                                "RBS",
                                "RP",
                                "SYM",
                                "TO",
                                "UH",
                                "VB",
                                "VBD",
                                "VBG",
                                "VBN",
                                "VBP",
                                "VBZ",
                                "WDT",
                                "WP",
                                "WP$",
                                "WRB",
                            ]
                        )
                    ),
                }
            ),                            
                supervised_keys=None,
                )
                
    def _split_generators(self, dl_manager: datasets.DownloadManager):

        train_path = dl_manager.download_and_extract(_TRAIN_DOWNLOAD_URL)
        dev_path = dl_manager.download_and_extract(_DEV_DOWNLOAD_URL)

        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepath": train_path}),
            datasets.SplitGenerator(name=datasets.Split.VALIDATION, gen_kwargs={"filepath": dev_path}),
        ]
        
    def _generate_examples(self, filepath):
        logger.info("generating examples from = %s", filepath)
        sid = 0
        tokens = []
        pos_tags = []
        #position = []

        with open(filepath, encoding="utf-8") as f:
            for line in f:
                if line[0]=='*':
                    if tokens != []:
                        yield sid, {
                                "tokens": tokens,
                                #"position": position,
                                "pos_tags": pos_tags,
                                #"sid": str(sid)
                                }
                        sid += 1
                        tokens = []
                        pos_tags = []
                        #position = []
                else:
                    line = line.split()
                    #position.append(line[0])
                    tokens.append(line[1])
                    pos_tags.append(line[2])

            yield sid, {
                        "tokens": tokens,
                        #"position": position,
                        "pos_tags": pos_tags,
                        #"sid": str(sid)
                        }





            

               

