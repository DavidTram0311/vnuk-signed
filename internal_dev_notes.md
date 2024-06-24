### Mark folder as:
- Source Root: `vnuk-signed`, `sign-language-production`, `text_translate`
- Excluded: `__pycache__`, `.idea` (follow [this instruction](https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore))  


#### Install CUDA BEFORE creating virtual environment:  
https://www.youtube.com/watch?v=d_jBX7OrptI&list=PLur6W2Lhl4UFHS0HTgMDfplOZ0040Lvx6


#### Install PyTorch AFTER installing CUDA:  
Note: check current CUDA version first
```Terminal (CMD on Windows is fine)
nvidia-smi
```
Then install PyTorch with the following command (check on [PyTorch website](https://pytorch.org/)):
```Terminal
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```
This project uses PyTorch for CUDA 12.1.  

#### Install packages manually (in order):
```
pip install py-trans
pip install aiofiles
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install -U setuptools wheel spacy
pip install datasets evaluate --upgrade
pip install spacy # this spacy should be installed as below
pip install torchtext
pip install pose-format
pip install simplemma
pip install matplotlib
```
Install spacy package: go to Python Packages --> search "spacy", click Install and wait for the IDE to work.  

