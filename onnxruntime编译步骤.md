
```bash
conda create -n onnxruntime python=3.8
pip install flatbuffers
conda activate onnxruntime
./build.sh --skip_tests --config Release --build_shared_lib --parallel
```
