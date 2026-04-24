import numpy as np
from particleloader import load

path = "/Users/nicholasdilullo/Desktop/research/LeBlancLab/datasets"

def download():
    for dtype in ["fp32", "fp16", "fp8e4m3fn"]:
        print(f"\nDownloading qg_jets_reduced [{dtype}]...")
        X, y = load("qg_jets_reduced", 2000000, cache_dir=path, dtype=dtype)
        print(f"  X shape: {X.shape}, y shape: {y.shape}")

RECORD_IDS = {
    "fp32": "19362155",
    "fp16": "19362553",
    "fp8e4m3fn": "19362689",
}

def verify():
    all_passed = True
    for dtype, record_id in RECORD_IDS.items():
        print(f"\nVerifying [{dtype}]...")
        for i in range(20):
            loader_file = f"{path}/qg_jets_reduced/dtype:{dtype}/QG_jets_{dtype}_{i}.npz"
            ref_file = f"{path}/{dtype}/{record_id}/QG_jets_{dtype}_{i}.npz"

            loader_data = np.load(loader_file)
            ref_data = np.load(ref_file)

            assert(np.array_equal(loader_data['X'], ref_data['X']))
            assert(np.array_equal(loader_data['y'], ref_data['y']))
            print(f"PASS file {i}")

    print("\nAll files match.")


def main():
    #download()
    verify()

if __name__ == "__main__":
    main()