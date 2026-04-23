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
    '[dtype:fp32]': [
        'fee5d383156c6ae5d16ea9f89dbf5a93',
        'c8729c8b0f4e614cde025618f97499cc',
        'c7aed82434530bfddfaf21bd5bc3bb21',
        '9dfdc199308960ff86a6836c8b56b4eb',
        '2fad5e83be2dc882081ed20c1326bdf4',
        '8b49219eda780e527cc8c26e8db99e82',
        '8b4edaf0d51822786292a86181a156fe',
        '038d87a2c9a5c21d9b81d39f0ab902bc',
        '99229ec71d731f073d234ca4615d186d',
        '104bca58cb34d01e73616f4a13a295c2',
        '29b4d62df4bfef61db41fae34a6e3d09',
        '819ed408db257c5b9c9a0d6e4342dd3a',
        'b32427d0941c37f8a5dc0ea2eae440a4',
        '3dc51f84007970b7a55326a7e974f0cb',
        '4dc2a08e048eb062a0bb2a18f80b088d',
        '8006c3580220dee876583b3210ed7e90',
        '2b31d72b51f1f2ad1d3ee09fadf18b52',
        'b6300b5b2e3fea39e932035ac7ba9d36',
        'a62edf7f14e9377b496c3d4ad0411657',
        'be969642ab8435c3658af15a3f88fa7e',
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
