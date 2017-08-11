# Mermaid (for Sublime)

> :tropical_fish: The missing [Sublime Text 3][] package for [Mermaid][].

```mermaid
%% Example code
graph BT
  ID-1[This is the text in the box]
  ID-2[This is the text in the box]
  ID-1---ID-2
  click ID-1 callback "Tooltip for a callback"

%% Example code
graph TB
  ID-1>This is the text in the box]
  ID-2>This is the text in the box]
  ID-1 --- ID-2
  click ID-1 "http://www.github.com" "This is a tooltip for a link"

%% Example code
graph TD
  ID-1(This is the text in the box)
  ID-2(This is the text in the box)
  ID-1---This is the text---ID-2

%% Example code
graph LR
  ID-1{This is the text in the box}
  ID-2{This is the text in the box}
  ID-1-->ID-2

%% Example code
graph RL
  ID-1((This is the text in the circle))
  ID-2((This is the text in the circle))
  ID-1 --- This is the text --> ID-2
```

[Sublime Text 3]: http://www.sublimetext.com
[Mermaid]: http://knsv.github.io/mermaid
