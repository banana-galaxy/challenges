solution = lambda v,w,V,W,s: (v+V if w+W<=s else 0 if w>s and W>s else v if w<=s and W>s or w<=s and W<=s and w+W>s and v>=V else V if w>s and W<=s or w<=s and W<=s and w+W>s and V>=v else 0)