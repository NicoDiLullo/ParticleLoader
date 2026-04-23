from particleloader.Datasets.Dataset import Dataset


ZENODO_URLS = {
    '[dtype:fp32]': [
        #TODO
    ],

    '[dtype:fp16]': [ #TODO


    ],

    '[dtype:fp8e4m3fn]': [ #TODO

    ],
}


hashes = {
    '[dtype:fp32]': [#TODO
            ],

    '[dtype:fp16]': [#TODO
            ],

    '[dtype:fp8e4m3fn]': [#TODO
        ],
}

qg_jets_reduced = Dataset(
    name = 'qg_jets_reduced',
    description = 'Quark and Gluon jets (reduced precision: fp32, fp16, fp8e4m3fn)',
    NUM_PER_FILE = 100000,
    NUM_FILES = 20,
    options = {"dtype": ["fp32", "fp16", "fp8e4m3fn"]},
    sources = ['zenodo'],
    shapes = [(150, 4), (1,)],
    npz_keys=['X', 'y'],
)

qg_jets_reduced.add_url('zenodo', ZENODO_URLS)
qg_jets_reduced.add_hash(hashes)
