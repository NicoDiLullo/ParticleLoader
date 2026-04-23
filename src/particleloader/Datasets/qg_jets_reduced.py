from particleloader.Datasets.Dataset import Dataset


ZENODO_URLS = {
    '[dtype:fp32]': [
        'https://zenodo.org/records/19362155/files/QG_jets_fp32_0.npz?download=1',
        'https://zenodo.org/records/19362155/files/QG_jets_fp32_1.npz?download=1',
        'https://zenodo.org/records/19362155/files/QG_jets_fp32_2.npz?download=1',
        'https://zenodo.org/records/19362155/files/QG_jets_fp32_3.npz?download=1',
        'https://zenodo.org/records/19362155/files/QG_jets_fp32_4.npz?download=1',
        'https://zenodo.org/records/19362155/files/QG_jets_fp32_5.npz?download=1',
        'https://zenodo.org/records/19362155/files/QG_jets_fp32_6.npz?download=1',
        'https://zenodo.org/records/19362155/files/QG_jets_fp32_7.npz?download=1',
        'https://zenodo.org/records/19362155/files/QG_jets_fp32_8.npz?download=1',
        'https://zenodo.org/records/19362155/files/QG_jets_fp32_9.npz?download=1',
        'https://zenodo.org/records/19362155/files/QG_jets_fp32_10.npz?download=1',
        'https://zenodo.org/records/19362155/files/QG_jets_fp32_11.npz?download=1',
        'https://zenodo.org/records/19362155/files/QG_jets_fp32_12.npz?download=1',
        'https://zenodo.org/records/19362155/files/QG_jets_fp32_13.npz?download=1',
        'https://zenodo.org/records/19362155/files/QG_jets_fp32_14.npz?download=1',
        'https://zenodo.org/records/19362155/files/QG_jets_fp32_15.npz?download=1',
        'https://zenodo.org/records/19362155/files/QG_jets_fp32_16.npz?download=1',
        'https://zenodo.org/records/19362155/files/QG_jets_fp32_17.npz?download=1',
        'https://zenodo.org/records/19362155/files/QG_jets_fp32_18.npz?download=1',
        'https://zenodo.org/records/19362155/files/QG_jets_fp32_19.npz?download=1',
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
