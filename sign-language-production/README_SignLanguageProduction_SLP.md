This pipeline serves the purpose of converting spoken text to sign language pose (OpenPose - 2D skeleton).  
More details of the project:  
1. Translate spoken text in any language to German/Swiss-German.
2. Text to Gloss: spoken German/Swiss-German text to corresponding gloss of Swiss-German Sign Language.
3. Gloss to Pose: Swiss-German Sign Language gloss to corresponding pose (OpenPose - 2D skeleton).

(Major) Pipeline components:  
- py-trans
- nmt (neural machine translation) glosser
- Pose lookup (to map gloss to pose) and smoothing (concatenate + smoothen)

Usage from terminal in `sign-language-production` directory:  
```python
# TODO: update this
```
