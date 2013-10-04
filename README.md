analyzefront
============

```
grep -r "def" . > ../def.txt
grep -r "render " . > ../render.txt
find . | grep "[.]js" > ../js.txt
find . | grep "[.]css" > ../css.txt
find . -size +5k > ../files.txt
find . -type f -exec wc -l {} \; > ../file_lines.txt
```

stylesheet_link_tag
javascript_include_tag
